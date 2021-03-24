from django.contrib import admin
from django.utils import timezone

from .models import Task


def task_finished(modeladmin, request, queryset):
    queryset.update(task_finished=True)
    queryset.update(finished_at=str(timezone.now()))


task_finished.short_description = "Mark selected tasks as done"


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'task_finished', 'creator', 'assigned_to', 'created_at', 'finished_at')
    list_filter = ['finished_at']
    order_by = ['finished_at', ]
    search_fields = ['title', 'assigned_to__username', 'creator__username' 'created_at']
    actions = [task_finished]
