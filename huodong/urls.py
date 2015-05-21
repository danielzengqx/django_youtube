from django.conf.urls import patterns, url, include
from huodong import views
urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
    url(r'^preview/',  views.preview, name='preview'),
    url(r'^submit/',  views.submit, name='submit'),
    url(r'^(?P<ref_id>.*)$', 'views.huodong', name='huodong'), 

	)
