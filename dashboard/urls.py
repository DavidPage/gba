from django.conf.urls import url

from dashboard import views

urlpatterns = [
    url(r'^$', views.index, name='dashboard'),
    url(r'^bank/new/', views.initialAmount, name='initialAmount'),
    url(r'^bank/add/$', views.insertInitialAmount, name='insertInitialAmount')
]