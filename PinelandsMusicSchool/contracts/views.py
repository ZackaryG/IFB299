from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Contract, Member


# Create your views here.
@login_required(login_url='../login/')
def contracts(request):
    if request.user.is_admin:
        all_teachers = Member.objects.all().filter(teacher=True)
        all_students = Member.objects.all().filter(teacher=False).filter(admin=False)
        context = {
            'all_teachers': all_teachers,
            'all_students': all_students
        }
        return render(request, 'contracts/contractcreation.html', context)
    else:
        return HttpResponseRedirect(reverse('home'))


def create_contract(request):
    if request.user.is_admin:
        teacher = Member.objects.filter(pk=request.POST.get('Teacher')).first()
        student = Member.objects.filter(pk=request.POST.get('Student')).first()

        contract = Contract(teacher=teacher, student=student)
        contract.save()

        return HttpResponseRedirect(reverse('contracts'))
    else:
        return HttpResponseRedirect(reverse('home'))
