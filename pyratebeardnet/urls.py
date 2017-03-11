"""
pyratebeardnet url Configuration

"""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('root.urls')),
    url(r'^code', include('c0de.urls')),
    url(r'^log', include('log.urls')),
    url(r'^mcc', include('mcc.urls')),
    url(r'^powerzone', include('powerzone.urls')),
]
