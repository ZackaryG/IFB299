from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def studentsignup(request):
    return render(request, 'studentsignup/studentsignuppage.html')