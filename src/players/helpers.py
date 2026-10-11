from teams.models import Team
import time, requests
from .models import *

NHL_WEB_API_BASE = "https://api-web.nhle.com/v1"


def _localized(value):
    """Return the English value used by the NHL Web API's localized fields."""
    if isinstance(value, dict):
        return value.get("default", next(iter(value.values()), ""))
    return value


def _player_landing(player_id):
    url = f"{NHL_WEB_API_BASE}/player/{player_id}/landing"
    return requests.get(url).json()


def updatePlayers():

    # trys, except the file doesnt exist
    try:
        with open("playerTime.txt", "r") as varsText:
            date = varsText.readline()
            date = int(float(date))
    except Exception:
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
            playerIds += getTeamRosterIds(team.abbreviation)
            # just so i dont get screwed for making too many requests
            time.sleep(0.1)

        for playerId in playerIds:

            playerStats = getPlayerStats(playerId)
            playerMetadata = getPlayerMetadata(playerId)
            playerData =  playerMetadata | playerStats

            print(playerData)

            if playerData.get("primaryPosition", {}).get("code") != "G":
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
    payload = _player_landing(id)
    stats = (payload.get("featuredStats") or {}).get("regularSeason", {}).get("subSeason") or {}
    if not stats:
        return {}

    # Keep the old model field names while adapting the current API names.
    return {
        "timeOnIce": stats.get("timeOnIce", ""),
        "assists": stats.get("assists", 0),
        "goals": stats.get("goals", 0),
        "pim": stats.get("pim", 0),
        "shots": stats.get("shots", 0),
        "games": stats.get("gamesPlayed", 0),
        "powerPlayGoals": stats.get("powerPlayGoals", 0),
        "powerPlayPoints": stats.get("powerPlayPoints", 0),
        "shortHandedGoals": stats.get("shorthandedGoals", stats.get("shortHandedGoals", 0)),
        "shortHandedPoints": stats.get("shorthandedPoints", stats.get("shortHandedPoints", 0)),
        "shotPct": stats.get("shootingPctg", stats.get("shotPct", 0)),
        "plusMinus": stats.get("plusMinus", 0),
        "points": stats.get("points", 0),
        "wins": stats.get("wins", 0),
        "losses": stats.get("losses", 0),
        "ot": stats.get("otLosses", 0),
        "shutouts": stats.get("shutouts", 0),
        "saves": stats.get("saves", 0),
        "savePercentage": stats.get("savePctg", stats.get("savePercentage", 0)),
        "goalsAgainst": stats.get("goalsAgainst", 0),
        "goalAgainstAverage": stats.get("goalsAgainstAvg", stats.get("goalAgainstAverage", 0)),
    }


def getPlayerMetadata(id):
    player = _player_landing(id)
    if not player:
        return {}

    team_id = player.get("currentTeamId", 0)
    team_abbreviation = player.get("currentTeamAbbrev", "")
    position = player.get("position") or player.get("positionCode")

    # Translate the new landing payload into the field names used by the
    # existing Player and Goalie models.
    return {
        "id": player.get("playerId", id),
        "firstName": _localized(player.get("firstName", "")),
        "lastName": _localized(player.get("lastName", "")),
        "number": player.get("sweaterNumber", 0),
        "birthDate": player.get("birthDate", ""),
        "birthCity": _localized(player.get("birthCity", "")),
        "birthCountry": player.get("birthCountry", ""),
        "nationality": player.get("birthCountry", ""),
        "height": str(player.get("heightInInches", "")),
        "weight": player.get("weightInPounds", 0),
        "shootsCatches": player.get("shootsCatches", ""),
        "currentTeam": {
            "id": team_id,
            "abbreviation": team_abbreviation,
            "name": _localized(player.get("fullTeamName", "")),
        },
        "teamId": team_id,
        "primaryPosition": {"code": position},
    }

# getting the ids of all the players on a given team
# helper function
def getTeamRosterIds(teamId):
    team_abbreviation = getattr(teamId, "abbreviation", teamId)
    url = f"{NHL_WEB_API_BASE}/roster/{team_abbreviation}/current"
    roster = requests.get(url).json()
    ids = []
    for position in ("forwards", "defensemen", "goalies"):
        ids.extend(player["id"] for player in roster.get(position, []))
    return ids