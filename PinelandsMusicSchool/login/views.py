from django.http import HttpResponse
from django.shortcuts import render
from login.forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_page(request):
    return render(request, 'C:/Users/zacka/Documents/GitHub/IFB299/PinelandsMusicSchool/login/templates/login.html')


def login_user(request):
    email = request.POST.get('Email')
    password = request.POST.get('Password')

    user = authenticate(username = email, password = password)

    if user is not None:
        login(request, user)
        return render(request, 'home/homepage.html')

    return render(request, 'C:/Users/zacka/Documents/GitHub/IFB299/PinelandsMusicSchool/login/templates/login.html')

def logout_user(request):
    logout(request)
    return render(request, 'home/homepage.html')