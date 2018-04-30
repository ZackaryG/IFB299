from django.http import HttpResponse
from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    a_student = Student.objects.all()[0]
    context = {
        'a_student': a_student,
    }
    return render(request, 'home\homepage.html', context)
