""" docstring """
from django.contrib import admin

from .models import Choice, Question

class ChoiceInLine(admin.StackedInline):
    """ class docstring """
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    """ class docstring """
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

# Register your models here.
admin.site.register(Choice)
admin.site.register(Question)
