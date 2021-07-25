from django.contrib import admin
from django.db import models
from django import forms

from .models import Quiz, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ 
        AnswerInline,
    ]


class QuestionInline(admin.TabularInline):
    model = Question 


class QuizAdmin(admin.ModelAdmin):
    inlines = [ 
        QuestionInline,
    ]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
