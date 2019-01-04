from django.db import models


class Event(models.Model):
    def info(self):
        print('Events')
