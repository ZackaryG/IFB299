from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def instrumentmanagement(request):
    return render(request, 'instrumentmanagement\instrumentmanagementpage.html')
