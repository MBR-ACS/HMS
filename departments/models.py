from django.db import models
from datetime import datetime, date
today = datetime.now()
# Create your models here.

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, help_text='enter department')
    created_at = models.DateTimeField(default=today)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name