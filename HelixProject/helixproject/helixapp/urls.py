from django.conf.urls import patterns, url
from helixapp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
		url(r'^game/$', views.game, name='game'),
		url(r'^game/new/$', views.game_new, name='new'),
		url(r'^game/solve/$', views.game_solve, name='solve'),
		url(r'^game/instructions/$', views.game_instructions, name='instructions'),
		url(r'^maps/$', views.maps, name='maps'),
		url(r'^history/$', views.history, name='history'),
		url(r'^history/generalInfo/$', views.history_generalInfo, name='generalInfo'),
		url(r'^history/current/$', views.history_current, name='current'),
		url(r'^history/favourites/$', views.history_favourites, name='favourites'),
		url(r'^camera/$', views.camera, name='camera'),
		url(r'^camera/selfie/$', views.selfie, name='selfie'),
		url(r'^camera/locations/$', views.locations, name='locations'),
		url(r'^camera/live/$', views.live, name='live'),
		url(r'^camera/location/', views.location, name='location'),
		url(r'^activities/$', views.activities, name='activities'),
		url(r'^emergency/$', views.emergency, name='emergency'),
	)
