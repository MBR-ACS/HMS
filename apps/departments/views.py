from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.departments.models import Department
from apps.departments.forms import DepartmentForm

# Create your views here.
def list_departments(request):
    departments = Department.objects.all()
    return render(request, 'departments/list_departments.html', context={'departments':departments})

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse("***Form Submitin successful***")
            return redirect('list-departments')
        else:
            return HttpResponse("***Your form is invaid***")
    if request.method == 'GET':
        form = DepartmentForm()
    return render(request, 'departments\create_department.html', context={'form':form})

def edit_department(request, dept_id):
    obj = Department.objects.get(dept_id=dept_id)
    form = DepartmentForm(instance=obj)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            #return HttpResponse("***Form Submitin successful***")
            return redirect('list-departments')
        else:
            return HttpResponse("***Your form is invaid***")
    return render(request, 'departments\create_department.html', context={'form':form})

def delete_department(request, dept_id):
    obj  = Department.objects.get(dept_id=dept_id)
    obj.delete()
    return redirect('list-departments')