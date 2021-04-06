from django.db import models

# Create your models here.
class Player(models.Model):

    # METADATA
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    number = models.IntegerField(default=0)

    birthDate = models.CharField(max_length=120)
    currentAge = models.IntegerField(default=0)
    birthCity = models.CharField(max_length=120)
    birthCountry = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    height = models.CharField(max_length=100)
    weight = models.IntegerField(default=0)

    alternateCaptain = models.BooleanField(default=False)
    captian = models.BooleanField(default=False)

    shootsCatches = models.CharField(max_length=1)

    currentTeam = models.JSONField(null=True)
    teamId = models.IntegerField(default=0)
    primaryPosition = models.JSONField(null=True)


    # STATS
    timeOnIce = models.CharField(max_length=120)

    assists = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    pim = models.IntegerField(default=0)
    shots = models.IntegerField(default=0)
    games = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)

    powerPlayGoals = models.IntegerField(default=0)
    powerPlayPoints = models.IntegerField(default=0)
    powerPlayTimeOnIce = models.CharField(max_length=120)

    shortHandedGoals = models.IntegerField(default=0)
    shortHandedPoints = models.IntegerField(default=0)
    shortHandedTimeOnIce = models.CharField(max_length=120)


    faceOffPct = models.DecimalField(decimal_places=1, max_digits=100, default=0)
    shotPct = models.DecimalField(decimal_places=1, max_digits=100, default=0)

    plusMinus = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    shifts = models.IntegerField(default=0)

    # USERS
    users = models.JSONField(null=True)

class Goalie(models.Model):

    # METADATA
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=120, default='')
    lastName = models.CharField(max_length=120, default='')
    number = models.IntegerField(default=0)

    birthDate = models.CharField(max_length=120, default='')
    currentAge = models.IntegerField(default=0)
    birthCity = models.CharField(max_length=120, default='')
    birthCountry = models.CharField(max_length=100, default='')
    nationality = models.CharField(max_length=100, default='')

    height = models.CharField(max_length=100, default='')
    weight = models.IntegerField(default=0)

    alternateCaptain = models.BooleanField(default=False)
    captian = models.BooleanField(default=False)

    shootsCatches = models.CharField(max_length=1, default='')

    currentTeam = models.JSONField(null=True)
    teamId = models.IntegerField(default=0)
    primaryPosition = models.JSONField(null=True)


    # STATS
    timeOnIce = models.CharField(max_length=120, default='')
    timeOnIcePerGame = models.CharField(max_length=120, default='')

    ot = models.IntegerField(default=0)
    shutouts = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    saves = models.IntegerField(default=0)
    powerPlaySaves = models.IntegerField(default=0)
    shortHandedSaves = models.IntegerField(default=0)
    evenSaves = models.IntegerField(default=0)

    shotsAgainst = models.IntegerField(default=0)    
    shortHandedShots = models.IntegerField(default=0)
    evenShots = models.IntegerField(default=0)
    powerPlayShots = models.IntegerField(default=0)

    savePercentage = models.DecimalField(decimal_places=14, max_digits=100, default=0)
    powerPlaySavePercentage = models.DecimalField(decimal_places=14, max_digits=100, default=0)
    shortHandedSavePercentage = models.DecimalField(decimal_places=14, max_digits=100, default=0)
    evenStrengthSavePercentage = models.DecimalField(decimal_places=14, max_digits=100, default=0)

    goalsAgainst = models.IntegerField(default=0)
    goalAgainstAverage = models.DecimalField(decimal_places=1, max_digits=100, default=0)

    games = models.IntegerField(default=0)
    gamesStarted = models.IntegerField(default=0) 

    # USERS
    users = models.JSONField(null=True)