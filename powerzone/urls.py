from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'powerzone.views.powerzone'),
)
