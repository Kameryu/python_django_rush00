from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.titlescreen),
	url(r'^[tT]itle[sS]creen$', views.titlescreen),
	url(r'^[wW]orldmap$', views.worldmap),
	url(r'^[bB]attle/', views.battle),
	url(r'^[mM]oviedex$', views.moviedex),
	url(r'^[mM]oviedex/', views.detail),
	url(r'^[oO]ptions$', views.option),
	url(r'^[oO]ptions/[sS]ave_[gG]ame$', views.save),
	url(r'^[oO]ptions/[lL]oad_[gG]ame$', views.load)
]
