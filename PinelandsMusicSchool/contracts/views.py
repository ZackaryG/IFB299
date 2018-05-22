from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def contracts(request):
    return render(request, 'contracts/contractcreation.html')
