from django.shortcuts import render
from teams.views import handlePost
from teams.helpers import *
from players.helpers import updatePlayers
from threading import *
from django.contrib.auth.decorators import login_required
from players.models import *
from django.http import HttpResponseRedirect


@login_required
def dashboardView(request):

    if request.method == "POST":
        handlePost(request)
        return HttpResponseRedirect(request.path)

    # pull data if needed
    t1 = Thread(target=getTeams, args=(request, ))
    t1.start()
    t2 = Thread(target=updatePlayers, args=(request, ))
    t2.start()

    # main view
    teams = list(Team.objects.all())
    userTeams = []
    for team in teams:
        if team.users and request.user.id in team.users:
            userTeams.append(team)

    players = list(Player.objects.all())
    userPlayers = []
    for player in players:
        if player.users and request.user.id in player.users:
            userPlayers.append(player)
    
    goalies = list(Goalie.objects.all())
    userGoalies = []
    for goalie in goalies:
        if goalie.users and request.user.id in goalie.users:
            userGoalies.append(goalie)

    context = {
        "teams": userTeams,
        "players": userPlayers,
        "goalies": userGoalies,
    }
    return(render(request, "dashboard/dashboard.html", context))
