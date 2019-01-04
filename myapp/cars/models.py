from django.db import models

# Create your models here.


class Car(models.Model):
    def info(self):
        print('Car')

    def __init__(self, engine):
        """Initializer."""
        self._engine = engine  # Engine is injected
