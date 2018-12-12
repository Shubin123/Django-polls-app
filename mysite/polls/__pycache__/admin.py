from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1
    list_display = ('question_text', 'pub_date')


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    
    list_display = ('question_text', 'pub_date',)
	
inlines = [ChoiceInline]


    
admin.site.register(Question, QuestionAdmin)