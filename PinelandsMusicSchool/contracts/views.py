from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
@login_required(login_url='../login/')
def contracts(request):
    if request.user.is_admin or request.user.is_teacher:
        return render(request, 'contracts/contractcreation.html')
    else:
        return HttpResponseRedirect(reverse('home'))
