from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Instrument
from django.urls import reverse

# Create your views here.
@login_required(login_url='../login/')
def instrumentmanagement(request):
    if request.user.is_admin or request.user.is_teacher:
        all_instruments = Instrument.objects.all()
        context = {'all_instruments': all_instruments}
        return render(request, 'instrumentmanagement\instrumentmanagementpage.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))

def add_instrument(request):
    if request.user.is_admin or request.user.is_teacher:
        type = request.POST.get('Instrument')
        size = request.POST.get('Size')
        quality = request.POST.get('Condition')
        available = request.POST.get('Available')
        rentalPrice = request.POST.get('RentalPrice')
        salePrice = request.POST.get('SalePrice')
        assignedStudent = request.POST.get('AssignedStudent')
        isSold = request.POST.get('IsSold')

        i = Instrument(type=type, size=size, quality=quality, available=available,
                       rental_price=rentalPrice, sale_price=salePrice,
                       assigned_student=assignedStudent, is_sold=isSold)
        i.save()
        return HttpResponseRedirect(reverse('instrumentmanagement'))
    else:
        return HttpResponseRedirect(reverse('home'))

def edit_instrument(request, id):
    if request.user.is_admin or request.user.is_teacher:
        i = Instrument.objects.get(pk = id)

        type = request.POST.get('Instrument')
        size = request.POST.get('Size')
        quality = request.POST.get('Condition')
        available = request.POST.get('Available')
        rentalPrice = request.POST.get('RentalPrice')
        salePrice = request.POST.get('SalePrice')
        assignedStudent = request.POST.get('AssignedStudent')
        isSold = request.POST.get('IsSold')

        i.save()

        return HttpResponseRedirect(reverse('instrumentmanagement'))
    else:
        return HttpResponseRedirect(reverse('home'))

def edit_form(request, id):
    if request.user.is_admin or request.user.is_teacher:
        context = {'instrument': Instrument.objects.get(pk = id)}
        return render(request, 'instrumentmanagement\edit_form.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))

def remove_instrument(request, id):
    if request.user.is_admin or request.user.is_teacher:
        i = Instrument.objects.get(pk = id)
        i.delete()
        return HttpResponseRedirect(reverse('instrumentmanagement'))
    else:
        return HttpResponseRedirect(reverse('home'))