from django.contrib import admin
from myapp.foo import models
from myapp.events import models as eventModel

admin.register(models.Foo)
admin.register(eventModel.Event)
