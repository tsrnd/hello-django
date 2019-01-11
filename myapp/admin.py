from django.contrib import admin
from myapp.foo import models

admin.site.register(models.Foo)
