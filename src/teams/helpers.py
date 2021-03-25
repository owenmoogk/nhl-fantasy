import requests
from .models import Team
import time

def getTeams(request):
    # trys, except the file doesnt exist
    try:
        with open("vars.txt", "r") as varsText:
            date = varsText.readline(0)
            date = int(date)
    except Exception:
        # create it, it is now 1970 /shrug
        with open("vars.txt", "w"):
            date = 0

    # ONLY RUNS THIS EVERY DAYISH
    if time.time()-86400 > date:

        # update the date file
        with open(".vars.txt", "w") as varsText:
            varsText.write(str(time.time()))

        baseUrl = "https://statsapi.web.nhl.com/"
        r = requests.get(baseUrl + '/api/v1/teams')
        originalData = r.json()
        originalData = originalData["teams"]
        for team in originalData:
            id = team["id"]
            try:
                databaseTeam = Team.objects.get(id = id)
            except Exception:
                Team.objects.create(id = id)
                databaseTeam = Team.objects.get(id = id)
            databaseTeam.name = team["name"]
            databaseTeam.abbreviation = team["abbreviation"]
            databaseTeam.link = team["link"]
            databaseTeam.save()

        print("done")