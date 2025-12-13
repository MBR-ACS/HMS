from django.db import models
# Create your models here.

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    phone = models.IntegerField(null=True)
    city = models.CharField(null=True)
    disease = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name