from django.conf.urls import url
from log.views import log, view_post, view_category

urlpatterns = [
    url(r'^$', log, name='log'),
    url(r'^/post/(?P<slug>[^\.]+).html', view_post, name='view_log_post'),
    url(r'^/category/(?P<slug>[^\.]+).html', view_category, name='view_log_category'),
]
