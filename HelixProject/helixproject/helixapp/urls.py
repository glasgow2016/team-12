from django.conf.urls import patterns, url
from helixapp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
		url(r'^game/$', views.game, name='game'),
		url(r'^game/new/$', views.gameNew, name='game'),
		url(r'^game/riddle/$', views.gameRiddle, name='game'),
		url(r'^game/instructions/$', views.gameInstructions, name='game'),
	)