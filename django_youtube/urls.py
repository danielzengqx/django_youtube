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
	url(r'^weixin$', 'joins.views.weixin', name='weixin'),
	url(r'^huodong/',include('huodong.urls',namespace="huodong")),

	# url(r'^huodong$', 'huodong.views.home', name='home'),	
	# url(r'^huodong/preview$', 'huodong.views.preview', name='preview'),	

	# "." means match any character , so anyother url should puth before this to match specific view#
    url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'), 




)

urlpatterns += static(settings.STATIC_URL, 
						document_root=settings.STATIC_ROOT)