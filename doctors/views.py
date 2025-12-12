from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def arthopedic(request):
    return HttpResponse('Hello from doctors app - arthopedic view')

def cardiology(request):
    return HttpResponse('Hello from doctors app - cardiology view')

def dermatology(request):
    return HttpResponse('Hello from doctors app - dermatology view')

def list_doc(request):
    return render(request, 'doctors/list_doctors.html')

def create_doctor(request):
    return render(request, 'doctors/create_doctor.html')