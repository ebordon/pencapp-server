from django.conf.urls import url, include
from pencapp import views

urlpatterns = [
    #url(r'^matchs/', views.match_list, name='match_list'),
    url(r'^next/', views.MatchList.as_view()),
    url(r'^played/', views.PlayedMatchesList.as_view()),
]
