from django.shortcuts import render
from apps.departments.models import Department

# Create your views here.
def list_departments(request):
    departments = Department.objects.all()
    return render(request, 'departments/list_departments.html', context={'departments':departments})