from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Team
from threading import *
from .helpers import *

@login_required
def myTeamView(request):
    t1 = Thread(target=getTeams, args=(request, ))
    t1.start()
    return(render(request, "teams/myTeams.html", {}))

@login_required
def allTeamView(request):
    return(render(request, "teams/allTeams.html", {}))