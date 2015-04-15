from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_youtube.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

 	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'joins.views.home', name='home'),
    url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='home'),

)

urlpatterns += static(settings.STATIC_URL, 
						document_root=settings.STATIC_ROOT)