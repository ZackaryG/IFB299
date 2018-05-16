from django.http import HttpResponse
from django.shortcuts import render
from .models import Animals

# Create your views here.
def home(request):
    a_student = Animals.objects.all()[0]
    context = {
        'a_student': a_student,
    }
    return render(request, 'home\homepage.html', context)
