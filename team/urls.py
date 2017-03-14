from django.conf.urls import url

from team import views

urlpatterns = [
    url(r'^$', views.index, name='team'),
    url(r'^new/$', views.new, name='newTeam'),
    url(r'^insert', views.insert, name='insertTeam'),
    url(r'^delete/(\d+)', views.delete, name='deleteTeam'),
]
