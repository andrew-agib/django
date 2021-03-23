from datetime import datetime

from django.contrib import admin

from .models import Task


# from django.contrib.auth.models import User


def task_finished(modeladmin, request, queryset):
    queryset.update(task_finished=True)
    queryset.update(finished=str(datetime.now()))


task_finished.short_description = "Mark selected tasks as done"


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    #def save_model(self, request, obj, form, change):
     #   if obj.user == request.user:
      #     pass
       # obj.save()

   # def get_changeform_initial_data(self, request):
    #    return {'user': request.user}
    list_display = ('__str__', 'title', 'task_finished', 'assigned', 'created', 'finished')
    list_filter = ['finished']
    order_by = ['finished', ]
    search_fields = ['title', 'assigned__username', 'created']
    actions = [task_finished]
    # if user.is_authenticated and request.user.is_superuser or user.is_authenticated and request.user == task.user %}


#admin.site.register(User)

# Register your models here.
