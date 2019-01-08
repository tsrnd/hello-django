from django.contrib import admin
from myapp.foo.models import Foo
from myapp.category.models import Category

admin.site.register(Foo)
admin.site.register(Category)
