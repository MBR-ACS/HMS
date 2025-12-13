from django.db import models
from doctors.models import Doctor

# Create your models here.
class Appointments(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=10, null=False)
    city = models.CharField(max_length=50, null=True)
    notes = models.TextField(null=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True) # if doctor is deleted this id will be null
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name