from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    # 필드 순서 변경하기
    # fields = ['question_text', 'pub_date']

    # 각 필드를 분리해서 보여주기
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)