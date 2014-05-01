from django.conf.urls import patterns, include, url

from django.contrib import admin
from core.views import logout_page, UserCreate

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'beers.views.home', name='home'),
# Login / logout, register.
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^register/$', UserCreate.as_view(), name='register'),
    url(r'^dashboard/$', 'beers.views.dashboard', name='dashboard'),
    url(r'^beer/', include('beers.urls', namespace='beer')),
    url(r'^keg/', include('kegs.urls', namespace='keg')),
    url(r'^tap/', include('taps.urls', namespace='tap')),
)
