from django.conf.urls import url
from root.views import root

urlpatterns = [
    url(r'^$', root, name='root'),
]
