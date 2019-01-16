from django.contrib import admin
from .poll.models import all as poll_models

for model in poll_models:
    admin.register(model)
    admin.site.register(model)
