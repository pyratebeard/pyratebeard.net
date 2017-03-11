from django.conf.urls import url
from c0de.views import code

urlpatterns = [
    url(r'^$', code, name='code'),
]
