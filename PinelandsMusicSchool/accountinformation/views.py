from django.http import HttpResponse
from django.shortcuts import render
from home.models import Student

# Create your views here.
def accountinformation(request):
    a_student = Student.objects.all()[0]
    context = {
        'a_student': a_student,
    }
    return render(request, 'accountinformation/accountinformationpage.html', context)

def timetable(request):
    return render(request, 'accountinformation/timetable.html')

def educationplan(request):
    return render(request, 'accountinformation/educationplan.html')
