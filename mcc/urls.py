from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'mcc.views.mcc'),
)
