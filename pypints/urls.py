from django.conf.urls import patterns, include, url

from django.contrib import admin
#from beers import views
from beers.views import BeerList, BeerDetail, BeerCreate, BeerUpdate
from beers.views import KegList, KegDetail, KegCreate, KegUpdate
from beers.views import TapList, TapUpdate
from beers.views import Beer_json
#from beers.views import BeerList

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pypints.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'beers.views.home', name='home'),
    url(r'^dashboard/$', 'beers.views.dashboard', name='dashboard'),
    url(r'^beer/list/$', BeerList.as_view(), name='beer_list'),
    url(r'^beer/create/$', BeerCreate.as_view(), name='beer_create'),
    url(r'^beer/update/(?P<pk>\d+)/$', BeerUpdate.as_view(), name='beer_update'),
    url(r'^beer/show/(?P<slug>[\w-]+)$', BeerDetail, name='beer_detail'),
    url(r'^beer/json/$', Beer_json, name='beer_json'),
    url(r'^keg/list/$', KegList.as_view(), name='keg_list'),
    url(r'^keg/show/(?P<pk>\d+)/$', KegDetail.as_view(), name='keg_detail'),
    url(r'^keg/create/$', KegCreate.as_view(), name='keg_create'),
    url(r'^keg/update/(?P<pk>\d+)/$', KegUpdate.as_view(), name='keg_update'),
    url(r'^tap/list/$', TapList.as_view(), name='tap_list'),
    url(r'^tap/update/(?P<pk>\d+)/$', TapUpdate.as_view(), name='tap_update'),
)
