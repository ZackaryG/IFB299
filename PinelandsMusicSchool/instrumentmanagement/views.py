from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Instrument
from django.urls import reverse

# Create your views here.
@login_required(login_url='../login/')
def instrumentmanagement(request):
    all_instruments = Instrument.objects.all()
    context = {'all_instruments': all_instruments}
    return render(request, 'instrumentmanagement\instrumentmanagementpage.html', context)

def add_instrument(request):
    type = request.POST.get('Instrument')
    size = request.POST.get('Size')
    quality = request.POST.get('Condition')
    available = request.POST.get('Available')
    rentalPrice = request.POST.get('RentalPrice')
    salePrice = request.POST.get('SalePrice')

    i = Instrument(type=type, size=size, quality=quality, available=available, rentalPrice=rentalPrice, salePrice=salePrice)
    i.save()
    return HttpResponseRedirect(reverse('instrumentmanagement'))

def remove_instrument(request, id):
    i = Instrument.objects.get(pk = id)
    i.delete()
    return HttpResponseRedirect(reverse('instrumentmanagement'))