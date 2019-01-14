from django.db import models
import datetime
from datetime import timedelta as tdelta
from django.utils import timezone



# Create your models here.
class Employees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    join_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        # return str(self.__class__) + '\n' + '\n'.join(
        #     ('{} = {}'.format(item, self.__dict__[item])
        #      for item in self.__dict__))
        return self.first_name, self.last_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.join_date <= now
