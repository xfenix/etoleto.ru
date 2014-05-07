from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView

from base.views import (NewsList, NewsDetail, ProductList,
                        WhereToBuyList, ProductDetail, RecipeList,
                        RecipeDetail)


admin.autodiscover()

urlpatterns = patterns('',
    # admin urls
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^admin/clear_cache/', 'misc.views.clear_cache'),
    url(r'^admin/', include(admin.site.urls)),

    # applications urls
    url(r'^$', 'base.views.index', name='index'),
    # news
    url(r'^news/$', NewsList.as_view(), name='news'),
    url(r'^news/(?P<pk>[0-9]+)/$', NewsDetail.as_view(), name='news-detail'),
    # recipes
    url(r'^recipes/$', RecipeList.as_view(), name='recipes'),
    url(r'^recipes/(?P<slug>.*?)/$', RecipeDetail.as_view(), name='recipes-detail'),
    # products
    url(r'^products/$', ProductList.as_view(), name='products'),
    url(r'^products/category/$', RedirectView.as_view(url='/products/')),
    url(r'^products/category/(?P<slug>.*?)/$', ProductList.as_view(), name='products-category'),
    url(r'^products/(?P<slug>.*?)/$', ProductDetail.as_view(), name='products-detail'),
    # where to buy
    url(r'^wheretobuy/$', WhereToBuyList.as_view(), name='wheretobuy'),
    # search page
    url(r'^search/$', 'base.views.search', name='search'),
)

handler404 = 'base.views.error_404'
handler500 = 'base.views.error_500'

if settings.DEBUG:
    from django.conf.urls.static import static
    st = static(settings.STATIC_URL, document_root=settings.CORE_PATH + '/static/')
    md = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + md + st

urlpatterns = urlpatterns + patterns('',
    # catch all pattern, after all try to match flatpage
    url(r'^(?P<url>.*/)$', 'misc.views.flatpage'),
)
