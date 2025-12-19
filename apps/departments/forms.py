from django import forms
from apps.departments.models import  Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']