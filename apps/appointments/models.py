from django.db import models
from apps.doctors.models import Doctor
from apps.patients.models import Patient
# Create your models here.
class Appointments(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True) # if doctor is deleted this id will be null
    appointment_date = models.DateTimeField()
    is_open = models.BooleanField(default=True) # appointment is completed or not
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.appointment_date.strftime("%d-%m-%Y %I:%M %p")