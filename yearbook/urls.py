from django.conf.urls import patterns, url, include
from yearbook import views
urlpatterns = patterns('',
	url(r'^$', views.home, name='home')
    # url(r'^$', views.list, name='list'),
    # urlrl(r'^upload_file$', views.upload_file, name='upload_file  '),
    # url(r'^list/$', views.home, name='list'),
	)
