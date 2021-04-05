from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from threading import *
from django.http import HttpResponseRedirect
from .helpers import updatePlayers


@login_required
def playerView(request, **kwargs):

    # pull data if needed
    t1 = Thread(target=updatePlayers)
    t1.start()

    playerId = kwargs["playerId"]
    try:
        player = Player.objects.get(id = playerId)
    except:
        player = 1
    context = {
        "id": player,
    }
    return(render(request, "players/players.html", context))