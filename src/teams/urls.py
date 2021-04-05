from django.conf.urls import include, url
from django.urls import path
from .views import *

urlpatterns = [
    url(r"^myTeams/", myTeamView),
    url(r"^allTeams/", allTeamView),
    path("team/<int:teamId>/", teamView),
]