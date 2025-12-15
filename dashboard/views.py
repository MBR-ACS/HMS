from django.shortcuts import render
from doctors.models import Doctor
from patients.models import Patient
from nurses.models import Nurses
from appointments.models import Appointments

# Create your views here.

def dashboard(request):
    '''this view renders the request and html template along with data'''
    doctor_count = Doctor.objects.count()
    patient_count = Patient.objects.count()
    nurse_count = Nurses.objects.count()
    appointment_count = Appointments.objects.count()

    data = {
        'doctor_cnt' : doctor_count, 
        'patients_cnt' : patient_count, 
        'nurse_cnt' : nurse_count,
        'appointment_cnt' : appointment_count,
        }

    return render(request, 'dashboard/dashboard.html', context=data)

def statictics():
    '''this function will generate only counts for all the model objects'''
    doctor_count = Doctor.objects.count()
    patient_count = Patient.objects.count()
    nurse_count = Nurses.objects.count()
    appointment_count = Appointments.objects.count()
    data = {
        'doctor_cnt' : doctor_count, 
        'patients_cnt' : patient_count, 
        'nurse_cnt' : nurse_count,
        'appointment_cnt' : appointment_count,
        }
    return data