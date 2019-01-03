from django.contrib import admin
from myapp.foo import models
from myapp.category import models as cate_models

admin.register(models.Foo)
admin.register(cate_models.Category)
