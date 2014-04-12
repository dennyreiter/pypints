from django.conf.urls import patterns, url

from .views import KegList, KegDetail, KegCreate, KegUpdate

urlpatterns = patterns('',

    url(r'^keg/list/$', KegList.as_view(), name='keg_list'),
    url(r'^keg/show/(?P<pk>\d+)/$', KegDetail.as_view(), name='keg_detail'),
    url(r'^keg/create/$', KegCreate.as_view(), name='keg_create'),
    url(r'^keg/update/(?P<pk>\d+)/$', KegUpdate.as_view(), name='keg_update'),
)
