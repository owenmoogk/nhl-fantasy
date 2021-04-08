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

    player = None
    error = ""
    playerType = ""

    try:
        player = Player.objects.get(id = playerId)
        playerType = "player"
    except:
        try:
            player = Goalie.objects.get(id = playerId)
            playerType = "goalie"
        except:
            error = "Player does not exist"

    playerDict = player.__dict__
    playerDict.pop("_state")
    playerDict.pop("users")

    context = {
        "player": player,
        "error": error,
        "playerType": playerType,
        "playerDict": playerDict,
    }
    return(render(request, "players/players.html", context))