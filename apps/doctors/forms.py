from django import forms
from apps.doctors.models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'email', 'phone', 'city', 'dept_id']
