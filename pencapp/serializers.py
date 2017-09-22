from rest_framework import serializers
from pencapp.models import Tournament, Match, Bet, Team


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ("name",)

class TournamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = ("name",)

class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = ('phase', 'team_one', 'team_two')
        depth = 1

class BetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bet
        fields = ('match', 'winner')
        depth = 1
