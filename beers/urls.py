from django.conf.urls import patterns, url

from .views import BeerList, BeerDetail, BeerCreate, BeerUpdate
from .views import Beer_json

urlpatterns = patterns('',
    url(r'^list/$', BeerList.as_view(), name='list'),
    url(r'^create/$', BeerCreate.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', BeerUpdate.as_view(), name='update'),
    url(r'^show/(?P<slug>[\w-]+)$', BeerDetail, name='detail'),
    url(r'^json/$', Beer_json, name='json'),
)
