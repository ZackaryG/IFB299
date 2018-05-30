"""PinelandsMusicSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.instrumentmanagement, name='instrumentmanagement'),
    path('add_instrument', views.add_instrument, name='add_instrument'),
    re_path(r'^edit_form/([0-9]+)$', views.edit_form, name='edit_form'),
    re_path(r'^remove_instrument/([0-9]+)$', views.remove_instrument, name='remove_instrument'),
    re_path(r'^edit_form/edit_instrument/([0-9]+)$', views.edit_instrument, name='edit_instrument'),
]
