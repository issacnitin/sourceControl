from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
import django.contrib.auth.views as auth_views
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'master/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'master/logout.html'}, name='logout')
]