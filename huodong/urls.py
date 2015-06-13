from django.conf.urls import patterns, url, include
from huodong import views
urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
    #url(r'^process_before_preview/$', views.process_before_preview, name='process_before_preview'),
    #url(r'^preview/(?P<huodong_id>\w{10})$',  views.preview, name='preview'),
    url(r'^preview/$',  views.preview, name='preview'),
    #url(r'^(release/?P<huodong_id>\w{10})$',  views.release, name='release'),
    url(r'^release/(?P<huodong_id>\w{10})$',  views.release, name='release'),

    #url(r'^(?P<ref_id>.*)$', 'views.huodong', name='huodong'), 

	)
