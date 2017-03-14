from django.conf.urls import url
from competition import views

urlpatterns = [
    url(r'^$', views.index, name='competition'),
    url(r'^New/$', views.new, name='newCompetition'),
    url(r'^Insert/$', views.insert, name='insertCompetition'),
    url(r'^Delete/(\d+)/$', views.delete, name='deleteCompetition'),
]
