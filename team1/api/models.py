from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    gender = models.BooleanField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name
