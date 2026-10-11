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

        # Current teams and their records are exposed by the NHL Web API's
        # standings endpoint. Team abbreviations are the API's stable key.
        url = "https://api-web.nhle.com/v1/standings/now"
        standings_data = requests.get(url).json().get("standings", [])

        for item in standings_data:
            team_abbreviation = item.get("teamAbbrev", {})
            if isinstance(team_abbreviation, dict):
                team_abbreviation = team_abbreviation.get("default")
            if not team_abbreviation:
                continue

            team_data = {
                "name": item.get("teamName", {}).get("default", ""),
                "gamesPlayed": item.get("gamesPlayed", 0),
                "wins": item.get("wins", 0),
                "losses": item.get("losses", 0),
                "ot": item.get("otLosses", 0),
                "pts": item.get("points", 0),
            }

            print(team_data)
            instance, created = Team.objects.get_or_create(abbreviation=team_abbreviation)
            for attr, value in team_data.items():
                setattr(instance, attr, value)
            instance.save()

        # Update the timestamp file
        with open("teamTime.txt", "w") as varsText:
            varsText.write(str(time.time()))