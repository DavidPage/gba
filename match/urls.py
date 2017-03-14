from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.match, name='match'),
    url(r'^New/$', views.new, name='new'),
    url(r'^Insert/$', views.insert, name='insert'),
    url(r'^Delete/(\d+)/$', views.delete, name='delete'),
]
