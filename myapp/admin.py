from django.contrib import admin
from .foo import models

class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text','pub_date']
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(models.Foo)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice)
