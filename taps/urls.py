from django.conf.urls import patterns, url

from .views import TapList, TapUpdate
from .views import RssTapFeed, AtomTapFeed

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pypints.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^tap/list/$', TapList.as_view(), name='tap_list'),
    url(r'^tap/update/(?P<pk>\d+)/$', TapUpdate.as_view(), name='tap_update'),
    url(r'^tap/rss/$', RssTapFeed()),
    url(r'^tap/atom/$', AtomTapFeed()),
)
