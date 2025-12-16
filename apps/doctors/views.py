from django.shortcuts import render
from django.http import HttpResponse
from apps.doctors.models import Doctor

# Create your views here.
def list_doctors(request):
    data = Doctor.objects.all()
    return render(request, 'doctors/list_doctors.html', context={"doctors": data})