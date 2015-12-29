from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_youtube.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

 	url(r'^admin', include(admin.site.urls)),
    url(r'^$', 'joins.views.home', name='home'),
    url(r'^kindle/$', 'joins.views.kindle', name='kindle'),
	url(r'^weixin$', 'joins.views.weixin', name='weixin'),
	#In Python regular expressions, the syntax for named regular-expression groups is (?P<name>pattern), \
	#where name is the name of the group and pattern is some pattern to matchself.
	url(r'^(?P<ref_id>\w{10})$', 'joins.views.share', name='share'),   	
	url(r'^huodong/',include('huodong.urls',namespace="huodong")),
	url(r'^yearbook/',include('yearbook.urls',namespace="yearbook")),
	# url(r'^huodong$', 'huodong.views.home', name='home'),	
	# url(r'^huodong/preview$', 'huodong.views.preview', name='preview'),	

	






)

urlpatterns += static(settings.STATIC_URL, 
						document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, 
						document_root=settings.MEDIA_ROOT)