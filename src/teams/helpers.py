import requests

def getTeams(request):
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
        x = databaseTeam.users
        x.append(request.user.id)
        databaseTeam.users = x
        databaseTeam.save()
    print("done dude")