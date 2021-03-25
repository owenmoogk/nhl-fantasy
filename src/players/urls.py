from django.conf.urls import include, url
from django.urls import path
from .views import *

urlpatterns = [
    path("roster/<int:teamId>/", rosterView, name="roster"),
    path("players/<int:playerId>/", playerView, name="player"),
]