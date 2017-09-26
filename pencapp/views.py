from django.http import HttpResponse, JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from pencapp.models import Match, Tournament, Team, Bet
from pencapp.serializers import MatchSerializer, TeamSerializer, BetSerializer, TournamentSerializer

class MatchList(APIView):
    #authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    #permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        next_games = Match.objects.filter(played=False).values('phase', 'schedule','team_one__name', 'team_two__name').order_by('phase', 'schedule')
        #matchs = [TeamSerializer(match.team_one).data for match in m]
        print(request.auth)
        return Response(next_games, headers={ "Access-Control-Allow-Origin": "*"})


class PlayedMatchesList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        played = Match.objects.filter(played=True).values('phase', 'schedule', 'team_one__name', 'team_two__name').order_by('phase', 'schedule')

        #matchs = [TeamSerializer(match.team_one).data for match in m]
        return Response(played, headers={ "Access-Control-Allow-Origin": "*"})


'''
@csrf_exempt
@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def match_list(request):
    """
    List all maatches.
    """
    if request.method == 'GET':
        matchs = Match.objects.all()
        serializer = MatchSerializer(matchs, many=True)
        return JsonResponse(serializer.data, safe=False)
'''
