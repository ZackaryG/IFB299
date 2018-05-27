from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacherapplication, name='teacherapplication'),
    path('add', views.add, name='add'),
]
