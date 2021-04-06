from teams.models import Team
import time, requests
from .models import *

def updatePlayers():

    # trys, except the file doesnt exist
    try:
        with open("playerTime.txt", "r") as varsText:
            date = varsText.readline()
            date = int(float(date))
    except Exception as e:
        # create it, it is now 1970 /shrug
        with open("playerTime.txt", "w"):
            date = 0

    # ONLY RUNS THIS EVERY DAYISH
    if time.time()-86400 > date: #fix

        print("getting the player data")

        # DOCUMENTATION
        # 1. Gets the ids for all active players, team by team
        # 2. For each player, gets the metadata and their stats, join together into single dictionary
        # 3. Put final dictionary into a model and save it

        # update the date file
        with open("playerTime.txt", "w") as varsText:
            varsText.write(str(time.time()))

        playerIds = []
        teams = Team.objects.all()

        for team in teams:
            teamId = team.id
            playerIds += getTeamRosterIds(teamId)
            # just so i dont get screwed for making too many requests
            time.sleep(0.1)

        for playerId in playerIds:

            playerStats = getPlayerStats(playerId)
            playerMetadata = getPlayerMetadata(playerId)
            playerData =  playerMetadata | playerStats

            print(playerData)

            if playerData["primaryPosition"]["code"] != "G":
                instance, created = Player.objects.get_or_create(id=playerId)
                for attr, value in playerData.items(): 
                    setattr(instance, attr, value)
                instance.save()

            else:
                instance, created = Goalie.objects.get_or_create(id=playerId)
                for attr, value in playerData.items(): 
                    setattr(instance, attr, value)
                instance.save()

# returning the players stats by id. If problem returns none
def getPlayerStats(id):
    baseUrl = "https://statsapi.web.nhl.com/"
    r = requests.get(baseUrl + "/api/v1/people/" + str(id) + "/stats?stats=statsSingleSeason&season=20202021")
    stats = r.json()
    try:
        stats = stats["stats"][0]["splits"][0]["stat"]
    except:
        stats = {}
    return(stats)

def getPlayerMetadata(id):
    baseUrl = "https://statsapi.web.nhl.com/"
    r = requests.get(baseUrl + "/api/v1/people/" + str(id))
    stats = r.json()
    try:
        stats = stats["people"][0]
        # just for ease of storage in django
        stats["number"] = stats["primaryNumber"]
        stats["teamId"] = stats["currentTeam"]["id"]
    except:
        stats = {}
    return(stats)

# getting the ids of all the players on a given team
# helper function
def getTeamRosterIds(teamId):
    baseUrl = "https://statsapi.web.nhl.com/"
    r = requests.get(baseUrl + "api/v1/teams/" + str(teamId) + "/roster")
    roster = r.json()
    roster = roster["roster"]
    ids = []
    for player in roster:
        ids.append(player["person"]["id"])
    return(ids)