from django.shortcuts import render
from doctors.models import Doctor
from patients.models import Patient
from nurses.models import Nurses
from departments.models import Department

# Create your views here.

def dashboard(request):
    doc_count = Doctor.objects.count()
    pt_count = Patient.objects.count()
    nrs_count = Nurses.objects.count()
    dpt_count = Department.objects.count()

    data = {'doctor' : doc_count, 'patients' : pt_count, 'nurse' : nrs_count,'department' : dpt_count,}

    return render(request, 'dashboard/dashboard.html', context=data)