from django.conf.urls import include, url
from django.urls import path
from .views import *

urlpatterns = [
    url("teams/", teamsView),
    path("team/<int:teamId>/", teamView),
]