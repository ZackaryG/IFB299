from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentsignup, name='studentsignup'),
    path('add', views.add, name='add'),
]