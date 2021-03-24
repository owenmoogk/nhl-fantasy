from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
 
# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=120)
    abbreviation = models.CharField(max_length=3)
    id = models.IntegerField(primary_key=True)
    link = models.CharField(max_length=120)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    users = models.JSONField(null = True)