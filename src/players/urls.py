from django.conf.urls import include, url
from django.urls import path
from .views import *

urlpatterns = [
    path("players/<int:playerId>/", playerView),
]