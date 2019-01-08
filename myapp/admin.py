from django.contrib import admin
from myapp.foo import models
from myapp.cars import cars as car
from myapp.snippets import models as snippet


admin.register(models.Foo)
admin.register(car.Car)
admin.register(snippet.Snippet)
