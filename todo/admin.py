from datetime import datetime

from django.contrib import admin

from .models import Task


def task_finished(modeladmin, request, queryset):
    queryset.update(task_finished=True)
    queryset.update(finished_at=str(datetime.now()))


task_finished.short_description = "Mark selected tasks as done"


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'task_finished', 'assigned_to', 'created_at', 'finished_at')
    list_filter = ['finished_at']
    order_by = ['finished_at', ]
    search_fields = ['title', 'assigned_to__username', 'created_at']
    actions = [task_finished]
