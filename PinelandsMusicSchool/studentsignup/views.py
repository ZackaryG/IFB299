from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from login.forms import *

# Create your views here.
def studentsignup(request):
    return render(request, 'studentsignup/studentsignuppage.html')


def add(request):
    email = request.POST.get('Email')
    first_name = request.POST.get('FirstName')
    last_name = request.POST.get('LastName')
    dob = request.POST.get('DOB')
    password = request.POST.get('Password')
    confirm_password = request.POST.get('ConfirmPassword')

    form = RegisterForm(request.POST)
    if form.is_valid():
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            Member.objects.create_student(email, first_name, last_name, dob, password, confirm_password)
            return render(request, 'login/login.html')

    return HttpResponseRedirect(reverse('studentsignup'))