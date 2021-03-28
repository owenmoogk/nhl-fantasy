from django.db import models

# Create your models here.
class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    number = models.IntegerField(default=0)
    teamId = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    pim = models.IntegerField(default=0)
    shots = models.IntegerField(default=0)
    users = models.JSONField(null=True)

class Goalie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    number = models.IntegerField(default=0)
    teamId = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    savePercentage = models.DecimalField(decimal_places=3, max_digits=1000)
    users = models.JSONField(null=True)