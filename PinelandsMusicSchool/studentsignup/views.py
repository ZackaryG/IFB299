from django.http import HttpResponse
from django.shortcuts import render
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

    Member.objects.create_student(email, first_name, last_name, dob, password)
    return render(request, 'studentsignup/studentsignuppage.html')