from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'beers.views.home', name='home'),
# Login / logout.
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'beers.views.logout_page'),
    url(r'^dashboard/$', 'beers.views.dashboard', name='dashboard'),
    url(r'^beer/', include('beers.urls', namespace='beer')),
    url(r'^keg/', include('kegs.urls', namespace='keg')),
    url(r'^tap/', include('taps.urls', namespace='tap')),
)
