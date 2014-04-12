from django.conf.urls import patterns, url

from .views import KegList, KegDetail, KegCreate, KegUpdate

urlpatterns = patterns('',

    url(r'^list/$', KegList.as_view(), name='list'),
    url(r'^show/(?P<pk>\d+)/$', KegDetail.as_view(), name='detail'),
    url(r'^create/$', KegCreate.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', KegUpdate.as_view(), name='update'),
)
