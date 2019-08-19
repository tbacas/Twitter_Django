
from django.urls import path
from . import views


urlpatterns = [
    path('', views.tweets, name='blog-home'),
]
