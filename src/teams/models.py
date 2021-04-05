from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
 
# Create your models here.
class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    abbreviation = models.CharField(max_length=3)
    firstYearOfPlay = models.IntegerField(default=0)
    officialSiteUrl = models.CharField(max_length=1000, default="")
    
    venue = models.JSONField(null = True)
    conference = models.JSONField(null = True)
    division = models.JSONField(null = True)

    gamesPlayed = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ot = models.IntegerField(default=0)
    pts = models.IntegerField(default=0)
    ptPctg = models.DecimalField(decimal_places=3, max_digits=100, default=0)

    goalsPerGame = models.DecimalField(decimal_places=3, max_digits=100, default=0)
    goalsAgainstPerGame = models.DecimalField(decimal_places=3, max_digits=100, default=0)

    powerPlayPercentage = models.DecimalField(decimal_places=3, max_digits=100, default=0)
    powerPlayGoals = models.DecimalField(decimal_places=3, max_digits=100, default=0)
    powerPlayGoalsAgainst = models.DecimalField(decimal_places=3, max_digits=100, default=0)
    penaltyKillPercentage = models.DecimalField(decimal_places=3, max_digits=100, default=0)

    shotsPerGame = models.DecimalField(decimal_places=4, max_digits=100, default=0)
    shotsAllowed = models.DecimalField(decimal_places=4, max_digits=100, default=0)
    savePctg = models.DecimalField(decimal_places=3, max_digits=100, default=0)

    faceOffsWon = models.IntegerField(default=0)
    faceOffsLost = models.IntegerField(default=0)
    faceOffWinPercentage = models.DecimalField(decimal_places=3, max_digits=100, default=0)

    users = models.JSONField(null=True)