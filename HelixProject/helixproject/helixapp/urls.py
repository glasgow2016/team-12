from django.conf.urls import patterns, url
from helixapp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
		url(r'^game/$', views.game, name='game'),
		url(r'^game/new/$', views.game_new, name='new'),
		url(r'^game/solve/$', views.game_solve, name='solve'),
		url(r'^game/instructions/$', views.game_instructions, name='instructions'),
	)