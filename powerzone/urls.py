from django.conf.urls import url
from powerzone.views import powerzone

urlpatterns = [
    url(r'^$', powerzone, name='powerzone'),
]
