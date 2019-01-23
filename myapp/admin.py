from django.contrib import admin
from .models.polls import *

admin.register(Question)
admin.register(Choice)

admin.site.register(Question)
admin.site.register(Choice)
