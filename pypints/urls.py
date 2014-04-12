from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'beers.views.home', name='home'),
    url(r'^dashboard/$', 'beers.views.dashboard', name='dashboard'),
    url(r'^beer/', include('beers.urls')),
    url(r'^keg/', include('kegs.urls')),
    url(r'^tap/', include('taps.urls')),
)
