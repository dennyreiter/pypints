from django.conf.urls import patterns, url

from .views import BeerList, BeerDetail, BeerCreate, BeerUpdate
from .views import Beer_json

urlpatterns = patterns('',
    url(r'^list/$', BeerList.as_view(), name='beer_list'),
    url(r'^create/$', BeerCreate.as_view(), name='beer_create'),
    url(r'^update/(?P<pk>\d+)/$', BeerUpdate.as_view(), name='beer_update'),
    url(r'^show/(?P<slug>[\w-]+)$', BeerDetail, name='beer_detail'),
    url(r'^json/$', Beer_json, name='beer_json'),
)
