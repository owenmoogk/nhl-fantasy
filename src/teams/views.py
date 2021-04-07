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
        obj = Team.objects.get(id = request.POST.get("id"))
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
    return(render(request, "teams/allTeams.html", context))


@login_required
def teamView(request, **kwargs):

    if request.method == "POST":
        handlePost(request)
        return HttpResponseRedirect(request.path)

    # pull data if needed
    t1 = Thread(target=getTeams, args=(request, ))
    t1.start()
    t2 = Thread(target=updatePlayers, args=(request, ))
    t2.start()

    id = kwargs["teamId"]

    try:
        team = Team.objects.get(id = id)
    except:
        context = {
            "error": "The team could not be found",
        }
        return(render(request, "teams/team.html", context))

    players = list(Player.objects.all())
    teamPlayers = []
    if players != None:
        for player in players:
            if player.teamId == id:
                teamPlayers.append(player)

    goalies = list(Goalie.objects.all())
    teamGoalies = []
    if goalies != None:
        for goalie in goalies:
            if goalie.teamId == id:
                teamGoalies.append(goalie)

    context = {
        "team": team,
        "players": teamPlayers,
        "goalies": teamGoalies,
    }

    return(render(request, "teams/team.html", context))