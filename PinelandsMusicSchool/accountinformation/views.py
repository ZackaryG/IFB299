from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='../login/')
def accountinformation(request):
    return render(request, 'accountinformation/accountinformationpage.html')

@login_required(login_url='../login/')
def timetable(request):
    return render(request, 'accountinformation/timetable.html')

@login_required(login_url='../login/')
def educationplan(request):
    return render(request, 'accountinformation/educationplan.html')
