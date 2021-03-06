"""gba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from gbauser import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Dashboard/$', include('dashboard.urls')),
    url(r'^Team/', include('team.urls')),
    url(r'^Competition/', include('competition.urls')),
    url(r'^Match/', include('match.urls')),
    url(r'^Market/', include('market.urls')),
    url(r'^Trade/', include('trade.urls')),
    url(r'^$', views.login_view, name="login"),
    url(r'^Logout/$', views.logout_view, name="logout"),
]
