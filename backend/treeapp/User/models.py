from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=500)
    xp = models.IntegerField()

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    level = models.IntegerField()
    xp = models.IntegerField()
    lvlxp = models.IntegerField()
    gold = models.IntegerField()
    day = models.IntegerField()
    cosmetics = models.JSONField()
    achievements = models.CharField(max_length=1000)
    tasks = models.ManyToManyField(Task)

    
