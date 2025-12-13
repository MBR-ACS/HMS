from django.db import models
from doctors.models import Doctor
# Create your models here.

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    phone = models.IntegerField(null=True)
    city = models.CharField(null=True)
    notes = models.TextField(null=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name