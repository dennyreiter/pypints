from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pypints.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'beers.views.home', name='home'),
    url(r'^dashboard/$', 'beers.views.dashboard', name='dashboard'),
    url(r'^beers', include('beers.urls')),
    url(r'^kegs', include('kegs.urls')),
    url(r'^taps', include('taps.urls')),
)
