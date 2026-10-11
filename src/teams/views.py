from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Team
from threading import *
from .helpers import *
from django.http import HttpResponseRedirect
from players.models import *
from players.views import *

def favorite(request):
    if request.POST.get("objectType") == "team":
        obj = Team.objects.get(abbreviation = request.POST.get("abbreviation"))
    elif request.POST.get("objectType") == "player":
        obj = Player.objects.get(id = request.POST.get("id"))
    elif request.POST.get("objectType") == "goalie":
        obj = Goalie.objects.get(id = request.POST.get("id"))

    userList = obj.users

    if userList == None:
        userList = []
        
    if request.user.id not in userList and "star" in request.POST:
        userList.append(request.user.id)
    if request.user.id in userList and "unstar" in request.POST:
        userList.remove(request.user.id)

    obj.users = userList
    obj.save()

def handlePost(request):
    if "star" in request.POST or "unstar" in request.POST:
        favorite(request)

@login_required
def teamsView(request):

    # if the user wants to save a team
    if request.method == "POST":
        handlePost(request)
        return HttpResponseRedirect(request.path)

    # pull data if needed
    t1 = Thread(target=getTeams, args=(request, ))
    t1.start()

    # main view
    data = Team.objects.all()
    context = {
        "teams": data,
    }
    return(render(request, "teams/teams.html", context))


@login_required
def teamView(request, **kwargs):

    if request.method == "POST":
        handlePost(request)
        return HttpResponseRedirect(request.path)

    # pull data if needed
    t1 = Thread(target=getTeams, args=(request, ))
    t1.start()
    t2 = Thread(target=updatePlayers)
    t2.start()

    team_id = kwargs["teamId"]

    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        context = {
            "error": "The team could not be found",
        }
        return(render(request, "teams/team.html", context))

    def belongs_to_team(player):
        current_team = player.currentTeam or {}
        return (
            current_team.get("abbreviation") == team.abbreviation
            or current_team.get("teamAbbrev") == team.abbreviation
        )

    players = list(Player.objects.all())
    teamPlayers = [player for player in players if belongs_to_team(player)]

    goalies = list(Goalie.objects.all())
    teamGoalies = [goalie for goalie in goalies if belongs_to_team(goalie)]

    context = {
        "team": team,
        "players": teamPlayers,
        "goalies": teamGoalies,
    }

    return(render(request, "teams/team.html", context))