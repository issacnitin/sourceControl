from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^thanks/$', views.thanks, name='thanks')
]