from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^(?P<id>\d+)$', views.get_post, name='post') 
]