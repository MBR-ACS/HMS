from django.shortcuts import render
from apps.patients.models import Patient

# Create your views here.
def list_patients(request):
    data = Patient.objects.all()
    return render(request, 'patients/list_patients.html', context={"patients": data})