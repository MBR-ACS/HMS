from django.db import models
from apps.departments.models import Department

# Create your models here.

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    city = models.CharField(max_length=50, null=True)
    dept_id = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name