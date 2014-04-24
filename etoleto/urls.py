from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from misc.views import flatpage


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'base.views.index', name='index'),

    # admin urls
    url(r'^admin/', include(admin.site.urls)),

    # catch all, try flatpage
    url(r'^(?P<url>.*/)$', flatpage),
)

handler404 = 'base.views.error_404'
handler500 = 'base.views.error_500'

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
