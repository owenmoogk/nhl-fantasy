from django.conf.urls import include, url
from django.urls import path
from .views import *

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
    url(r"^account/", account),
    url(r"^change-password", changePassword),
    path("home/", homeView),
    path("", homeView),
]