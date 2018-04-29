from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # Executes method views.index when called
]