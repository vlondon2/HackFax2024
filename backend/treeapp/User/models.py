from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    level = models.IntegerField()
    xp = models.IntegerField()
    lvlxp = models.IntegerField()
    gold = models.IntegerField()
    cosmetics = models.CharField(max_length=1000)
    achievements = models.CharField(max_length=1000)
    tasks = models.CharField(max_length=1000)

    
