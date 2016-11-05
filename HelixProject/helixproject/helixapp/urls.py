from django.conf.urls import patterns, url
from helixapp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
		url(r'^game/$', views.game, name='game'),
		url(r'^game/new/$', views.game_new, name='game'),
		url(r'^game/riddle/$', views.game_riddle, name='game'),
		url(r'^game/instructions/$', views.game_instructions, name='game'),
	)