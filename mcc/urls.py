from django.conf.urls import url
from mcc.views import mcc

urlpatterns = [
    url(r'^$', mcc, name='mcc'),
]
