from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'log.views.log'),
    url(r'^/post/(?P<slug>[^\.]+).html', 'log.views.view_post', name='view_log_post'),
    url(r'^/category/(?P<slug>[^\.]+).html', 'log.views.view_category', name='view_log_category'),
)
