from django.contrib import admin

# Register your models here.
from api.entities.product_entities import Product

admin.site.register(Product)
