from django.urls import path
from apps.appointments.views import list_all_appointments

urlpatterns = [
    path('list_appointments/', list_all_appointments, name='list-appointments')
]