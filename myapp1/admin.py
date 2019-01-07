from django.contrib import admin
from myapp1.question_choice.models import Choice, Question

# Register your models here.
admin.site.register(Choice)
admin.site.register(Question)
