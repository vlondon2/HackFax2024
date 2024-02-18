from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    level = models.IntegerField()
    xp = models.IntegerField()
    lvlxp = models.IntegerField()
    gold = models.IntegerField()
    cosmetics = models.CharField(max_length=1000, default='')
    achievements = models.CharField(max_length=1000, default='')
    tasks = models.CharField(max_length=1000, default='')
    taskCount = models.IntegerField(default=0)
    newbie = models.BooleanField(default=False)
    bronzeMedal = models.BooleanField(default=False)
    silverMedal = models.BooleanField(default=False)
    goldMedal = models.BooleanField(default=False)
    highRoller = models.BooleanField(default=False)


    
