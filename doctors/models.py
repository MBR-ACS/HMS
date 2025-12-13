from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    city = models.CharField(null=True)
    dept = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name