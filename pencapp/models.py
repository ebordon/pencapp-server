from django.db import models

#those imports are because we choose to have authentication by token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# After create a user, adds the token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Tournament(models.Model):
    name = models.CharField(max_length=50)
    finished = models.BooleanField(default=False)

    def hasFinished(self):
        if self.finished:
            return "Finalizado"
        else:
            return "En curso"

    def __str__(self):
        return "{}. {}".format(self.name, self.hasFinished())

class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Match(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tournament = models.ForeignKey(Tournament)
    team_one = models.ForeignKey(Team, related_name='team_one')
    team_two = models.ForeignKey(Team, related_name='team_two')
    schedule = models.DateTimeField(null=True, blank=True)
    place = models.CharField(max_length=50)
    played = models.BooleanField(default=False)
    winner = models.ForeignKey(Team,null=True, blank=True, default=None, related_name='winner')
    phase = models.IntegerField()

    def __str__(self):
        return "Fecha {} - {} vs {} en {}.".format(self.phase, self.team_one, self.team_two, self.place)

    class Meta:
        ordering = ('created',)

class Bet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    match_id = models.ForeignKey(Match)
    winner = models.ForeignKey(Team)
