from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Team
from threading import *
from .helpers import *
from django.http import HttpResponseRedirect

@login_required
def myTeamView(request):

    if request.method == "POST":
        if "unstar" in request.POST:
            obj = Team.objects.get(id = request.POST.get("id"))
            userList = obj.users
            userList.remove(request.user.id)
            obj.users = userList
            obj.save()
            
        # redirects here in a get request... fixes refresh problem
        return HttpResponseRedirect('/myTeams')

    # pull data if needed
    t1 = Thread(target=getTeams, args=(request, ))
    t1.start()

    # main view
    teams = list(Team.objects.all())
    data = []
    # appending the teams that the user has saved
    if teams != None:
        for team in teams:
            if team.users:
                if request.user.id in team.users:
                    data.append(team)
    context = {
        "teams": data,
    }
    return(render(request, "teams/myTeams.html", context))


@login_required
def allTeamView(request):

    # pull data if needed
    t1 = Thread(target=getTeams, args=(request, ))
    t1.start()

    # if the user wants to save a team
    if request.method == "POST":
        if "star" in request.POST:
            obj = Team.objects.get(id = request.POST.get("id"))
            userList = obj.users
            if userList == None:
                userList = []
            if request.user.id not in userList:
                userList.append(request.user.id)
            obj.users = userList
            obj.save()
        
        if "unstar" in request.POST:
            obj = Team.objects.get(id = request.POST.get("id"))
            userList = obj.users
            userList.remove(request.user.id)
            obj.users = userList
            obj.save()

        # redirects here in a get request... fixes refresh problem
        return HttpResponseRedirect('/allTeams')

    # main view
    data = Team.objects.all()
    context = {
        "teams": data,
    }
    return(render(request, "teams/allTeams.html", context))