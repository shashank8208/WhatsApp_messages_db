from unicodedata import name
from django import urls
from django.contrib import admin
from django.urls import path
from message import views

urlpatterns = [
    path("webhook",views.message),
]