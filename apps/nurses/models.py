from django.db import models

# Create your models here.
class Nurses(models.Model):
    nurse_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=10, null=False)
    email = models.EmailField(unique=True, null=False)
    city = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name