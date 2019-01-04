from django.contrib import admin
from .foo import models

admin.site.register(models.Foo)
admin.site.register(models.Question)
admin.site.register(models.Choise)
