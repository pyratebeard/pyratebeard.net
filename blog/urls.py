from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'blog.views.blog'),
)
