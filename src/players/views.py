from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from teams.models import Team
from threading import *
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def rosterView(request, **kwargs):
    teamId = kwargs["teamId"]
    print(teamId)
    context = {
        "id": teamId,
    }
    return(render(request, "players/players.html", context))


@login_required
def playerView(request, **kwargs):
    playerId = kwargs["playerId"]
    context = {
        "id": playerId,
    }
    return(render(request, "players/players.html", context))