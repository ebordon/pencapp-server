from django.conf.urls import url, include
from pencapp import views

urlpatterns = [
    url(r'^$', views.match_list, name='match_list'),
]
