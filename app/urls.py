from django.contrib import admin
from django.urls import path
from .views import home,add_user


urlpatterns = [
    path('',home),
    path('add_user',add_user),
]