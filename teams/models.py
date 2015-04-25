from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    institution = models.CharField(max_length=124) # university where team is from
    tag = models.CharField(max_length=16)
    description = models.TextField(max_length=1024)
    logo = models.ImageField()
    players = models.ManyToManyField(User, through='Player')

    def __str__(self):
        return self.name


class PlayerManager(models.Manager):
    use_for_related_fields = True

    def add_player(self, user, team):
        if not user.team:
            team.players.add(user)

    def remove_player(self, user, team):
        team.players.remove(user)


class Player(models.Model):
    user = models.OneToOneField(User)
    team = models.ForeignKey('Team')

    objects = PlayerManager()

    def __str__(self):
        return self.user.username
