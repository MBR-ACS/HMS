from django.shortcuts import render
from django.http import HttpResponse
from apps.doctors.models import Doctor
from apps.doctors.forms import DoctorForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list_doctors(request):
    data = Doctor.objects.all()
    return render(request, 'doctors/list_doctors.html', context={"doctors": data})

@login_required
def create_doctor(request):
    form = DoctorForm()
    return render(request, 'doctors/create_doctor.html', context={'form':form})