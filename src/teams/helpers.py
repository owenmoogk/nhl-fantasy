import requests
from .models import Team
import time

def getTeams(request):
    # Check/create sync tracking file
    try:
        with open("teamTime.txt", "r") as varsText:
            date = int(float(varsText.readline()))
    except Exception:
        with open("teamTime.txt", "w"):
            date = 0

    # Runs once a day-ish
    if time.time() - 86400 > date:
        print("Getting team standings and metadata...")

        # Modern Web API standings endpoint
        url = "https://api-web.nhle.com/v1/standings/now"
        r = requests.get(url)
        standings_data = r.json().get("standings", [])

        for item in standings_data:
            team_id = item.get("teamAbbrev", {}).get("default")
            team_data = {
                "id": team_id,
                "teamName": item.get("teamName", {}).get("default"),
                "teamAbbrev": team_id,
                "wins": item.get("wins"),
                "losses": item.get("losses"),
                "ot": item.get("otLosses"),
                "pts": item.get("points"),
                "goalDifferential": item.get("goalDifferential"),
            }

            print(team_data)
            instance, created = Team.objects.get_or_create(abbreviation=team_id)
            for attr, value in team_data.items():
                if hasattr(instance, attr):
                    setattr(instance, attr, value)
            instance.save()

        # Update the timestamp file
        with open("teamTime.txt", "w") as varsText:
            varsText.write(str(time.time()))