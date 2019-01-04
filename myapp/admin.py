from django.contrib import admin
from myapp.foo import models
from myapp.events import models as eventModel
from myapp.cars import models as car


admin.register(models.Foo)
admin.register(eventModel.Event)
admin.register(car.Car)
