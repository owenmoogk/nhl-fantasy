import requests
from .models import Team
import time

def getTeams(request):

    # trys, except the file doesnt exist
    try:
        with open("teamTime.txt", "r") as varsText:
            date = varsText.readline()
            date = int(float(date))
    except Exception:
        # create it, it is now 1970 /shrug
        with open("teamTime.txt", "w"):
            date = 0

    # ONLY RUNS THIS EVERY DAYISH
    if time.time()-86400 > date:

        print("getting the team data")

        # DOCUMENTATION
        # 1. Get all the teams metadata
        # 2. For each team, get the id and retrieve the stats for the corresponding id
        # 3. Make a final dictionary called teamData, which contains both the metadata and the stats of the team (joining dictionaries with | operator)
        # 4. save the instance with code from stack overflow :)

        # update the date file
        with open("teamTime.txt", "w") as varsText:
            varsText.write(str(time.time()))

        baseUrl = "https://statsapi.web.nhl.com/"
        r = requests.get(baseUrl + '/api/v1/teams')
        originalData = r.json()
        originalData = originalData["teams"]
        # originalData is the dictionary containing all the metadata of all the teams

        # team is the dictionary with the current teams metadata
        for team in originalData:
            print("gettng teaim data")
            # getting the stats for the current team
            currTeamId = team["id"]
            teamStats = getTeamStats(currTeamId)

            # combining the team metadata with the stats for the final dictionary
            teamData = team | teamStats
            
            # https://stackoverflow.com/questions/5503925/how-do-i-use-a-dictionary-to-update-fields-in-django-models
            instance, created = Team.objects.get_or_create(id=currTeamId)
            for attr, value in teamData.items(): 
                setattr(instance, attr, value)
            instance.save()


# gets the stats of the team, returns as a dictionary
def getTeamStats(id):
    baseUrl = "https://statsapi.web.nhl.com/"
    r = requests.get(baseUrl + '/api/v1/teams/' + str(id) + "/stats")
    teamData = r.json()
    teamData = teamData["stats"][0]["splits"][0]["stat"]
    return(teamData)