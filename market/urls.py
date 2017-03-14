from django.conf.urls import url
from market import views

urlpatterns = [
    url(r'^$', views.markets, name='markets'),
    url(r'^new', views.new, name='newMarket'),
    url(r'^insert', views.insert, name='insertMarket'),
    url(r'^Delete/(\d+)', views.delete, name='deleteMarket'),
]
