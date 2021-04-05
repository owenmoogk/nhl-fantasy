from teams.models import Team
import time, requests
from .models import *

baseUrl = "https://statsapi.web.nhl.com/"

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
    if time.time()-86400 > date:
        print("updating players")
        # update the date file
        with open("playerTime.txt", "w") as varsText:
            varsText.write(str(time.time()))

        teams = Team.objects.all()
        # the players will be stored in list of dictionarys, storing key value pairs which will later be put into the model
        playerDicts = []
        for team in teams:
            teamId = team.id
            playerDicts += getTeamRosterIds(teamId)
            time.sleep(0.1)

        for player in playerDicts:
            # player is the dictionary
            stats = getPlayerStatsById(player["id"])

            if stats == None:
                continue

            try:
                player['assists'] = stats['assists']
                player['goals'] = stats['goals']
                player['pim'] = stats['pim']
                player['shots'] = stats['shots']
                player['points'] = stats['points']

                try:
                    currPlayer = Player.objects.create(**player)
                except:
                    currPlayer = Player.objects.get(id = player["id"])
                    currPlayer = Player(**player)
                finally:
                    currPlayer.save()

            # player is a goalie
            except Exception:
                try:
                    player["wins"] = stats["wins"]
                    player["losses"] = stats["losses"]
                    player['savePercentage'] = stats['savePercentage']

                    try:
                        currPlayer = Goalie.objects.create(**player)
                    except:
                        currPlayer = Goalie.objects.get(id = player["id"])
                        currPlayer = Goalie(**player)
                    finally:
                        currPlayer.save()

                except Exception as e:
                    print("had an error getting the data into the database")
                    print(e)
                    print(player["id"])
                    print(stats)


# this might be a problem, i might have to add in some delay to not get an error for accessing too fast
def getPlayerStatsById(id):
    r = requests.get(baseUrl + "/api/v1/people/" + str(id) + "/stats?stats=statsSingleSeason&season=20202021")
    stats = r.json()
    try:
        stats = stats["stats"][0]["splits"][0]["stat"]
    except:
        stats = None
    return(stats)

def getTeamRosterIds(teamId):
    r = requests.get(baseUrl + "api/v1/teams/" + str(teamId) + "/roster")
    roster = r.json()
    # i dont need the copyright, only care about the roster
    roster = roster["roster"]
    # getting rid of the person label
    for index, player in enumerate(roster):
        tmp = {
            "id": player["person"]["id"],
            "name": player["person"]["fullName"],
            "number": player["jerseyNumber"],
            "teamId": teamId,
        }
        roster[index] = tmp
    return(roster)