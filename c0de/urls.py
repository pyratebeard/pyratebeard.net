from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'c0de.views.code'),
)
