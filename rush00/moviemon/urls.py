from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.titlescreen),
    url(r'^worldmap/$', views.worldmap),
    url(r'^worldmap/(?P<param>up|down|left|right|a|b)/$', views.worldmap),
    url(r'^battle/(?P<moviemon_id>tt[0-9]+)/$', views.battle),
    url(r'^battle/(?P<moviemon_id>tt[0-9]+)/(?P<param>catch)/$', views.battle),
    url(r'^moviedex/$', views.moviedex),
    url(r'^moviedex/(?P<moviemon>tt[0-9]+)$', views.moviedex),
    url(r'^options/$', views.options),
    url(r'^options/save_game/$', views.save_game),
    url(r'^options/load_game/$', views.load_game),
    url(r'^options/load_game/(?P<param>up|down|load|start_game)/$', views.load_game),
]
