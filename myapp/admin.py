from django.contrib import admin
from myapp.foo import models
from myapp.cars import cars as car
from myapp.bookshelf import models as book


admin.register(models.Foo)
admin.register(car.Car)
admin.register(book.Author)
admin.register(book.Book)