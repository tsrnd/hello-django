from django.db import models


# Create your models here.
class Employees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    join_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
