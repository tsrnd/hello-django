from django.contrib import admin
from myapp.foo import models
from myapp.cars import cars as car


admin.register(models.Foo)
admin.register(car.Car)
