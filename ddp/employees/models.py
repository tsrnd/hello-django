from django.db import models

# Create your models here.


class Employees(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)

    class Meta:
        managed = False
        # Table name
        db_table = 'employees'
