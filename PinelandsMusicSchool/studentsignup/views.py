from django.http import HttpResponse
from django.shortcuts import render
from home.models import Student

# Create your views here.
def studentsignup(request):
    return render(request, 'studentsignup/studentsignuppage.html')