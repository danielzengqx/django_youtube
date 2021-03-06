from django.conf.urls import patterns, url, include
from huodong import views
urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
    #url(r'^process_before_preview/$', views.process_before_preview, name='process_before_preview'),
    #url(r'^preview/(?P<huodong_id>\w{10})$',  views.preview, name='preview'),
    url(r'^preview*/$',  views.preview, name='preview'),
    #url(r'^(release/?P<huodong_id>\w{10})$',  views.release, name='release'),
    url(r'^release/(?P<user_id>\w{28})/(?P<huodong_id>\w{10})$',  views.release, name='release'),
    url(r'^success/$',  views.success, name='success'),
    url(r'^mine/$',  views.mine, name='mine'),
    url(r'^join/.*$',  views.join, name='join'),
    url(r'^qr/$',  views.qr, name='qr'),
    url(r'^csv/$', views.write_csv, name='write_csv'),
    url(r'^yearbook/(?P<user_id>\w{10})$', views.yearbook, name='yearbook'),
    url(r'^yearbook/(?P<user_id>\w{10})/show$', views.show, name='show'),
    # url(r'^(?P<ref_id>.*)$', 'views.huodong', name='huodong'), 

	)
