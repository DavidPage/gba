from django.conf.urls import url
from trade import views

urlpatterns = [
    url(r'^$', views.trades, name='trades'),
    url(r'^PopulateDB', views.populatedb, name='populatedb'),
    url(r'^New', views.new, name='newTrade'),
    url(r'^Insert', views.insert, name='insertTrade'),
    url(r'^Delete/(\d+)', views.delete, name='deleteTrade'),
    url(r'^filterByMonth/(\d+)', views.filterByMonth, name='filterByMonth'),
]
