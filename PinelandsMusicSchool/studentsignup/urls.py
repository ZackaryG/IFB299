from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentsignup, name='studentsignup'),
    path('add_student', views.add_student, name='add_student'),
]
