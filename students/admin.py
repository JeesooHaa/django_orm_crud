from django.contrib import admin
from .models import Student

@admin.register(Student)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'birthday', 'age',)
