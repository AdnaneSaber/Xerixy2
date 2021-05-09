from django.contrib import admin
from .models import Task


class TasksAdmin(admin.ModelAdmin):
    list_display = ['title', 'done', 'end_date', 'priority']


admin.site.register(Task, TasksAdmin)
