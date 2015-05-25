from django.conf.urls import patterns, url, include
from huodong import views
urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
    url(r'^preview/$',  views.preview, name='preview'),
    #url(r'^(release/?P<huodong_id>\w{10})$',  views.release, name='release'),
    url(r'^release/$',  views.release, name='release'),
    #url(r'^(?P<ref_id>.*)$', 'views.huodong', name='huodong'), 

	)
