from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    institution = models.CharField(max_length=124) # university where team is from
    tag = models.CharField(max_length=16)
    description = models.TextField(max_length=1024)
    logo = models.ImageField()

class Player(models.Model):
    user = models.OneToOneField(User)
    team = models.ForeignKey('Team')
