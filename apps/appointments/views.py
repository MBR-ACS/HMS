from django.shortcuts import render
from apps.appointments.models import Appointments

# Create your views here.
def list_all_appointments(request):
    data = Appointments.objects.all()
    # data = Appointments.objects.filter(is_open=False)
    return render(request, 'appointments/list_all_appointments.html', context={'appointments':data})
