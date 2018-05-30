from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacherapplication, name='teacherapplication'),
    path('add_teacher', views.add_teacher, name='add_teacher'),
]
