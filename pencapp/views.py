from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from pencapp.models import Match, Tournament, Team, Bet
from pencapp.serializers import MatchSerializer, TeamSerializer, BetSerializer, TournamentSerializer

@csrf_exempt
def match_list(request):
    """
    List all maatches.
    """
    if request.method == 'GET':
        matchs = Match.objects.all()
        serializer = MatchSerializer(matchs, many=True)
        return JsonResponse(serializer.data, safe=False)

    #elif request.method == 'POST':
    #    data = JSONParser().parse(request)
    #    serializer = SnippetSerializer(data=data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return JsonResponse(serializer.data, status=201)
    #    return JsonResponse(serializer.errors, status=400)
