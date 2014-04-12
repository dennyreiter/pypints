from django.conf.urls import patterns, url

from .views import TapList, TapUpdate
from .views import RssTapFeed, AtomTapFeed

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pypints.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^list/$', TapList.as_view(), name='list'),
    url(r'^update/(?P<pk>\d+)/$', TapUpdate.as_view(), name='update'),
    url(r'^rss/$', RssTapFeed()),
    url(r'^atom/$', AtomTapFeed()),
)
