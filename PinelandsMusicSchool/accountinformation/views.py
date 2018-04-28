from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def accountinformation(request):
    return render(request, 'accountinformation/accountinformationpage.html')
