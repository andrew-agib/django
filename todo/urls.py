from django.urls import path

from . import views

urlpatterns = [
    path('tasksilteredbyuser/', views.filtered_tasks),
    path('tasksjsonresponse/', views.tasks_get, name='get'),
    path('taskresponse/', views.tasks_drf, name='get'),
    path('userresponse/', views.user_drf, name='get'),
    path('userclasspaginated/', views.UserList.as_view()),
    path('taskclasspaginated/', views.TaskList.as_view()),
    path('taskapi/', views.TaskAPI.as_view(), name='task_api'),
    path('filter/', views.search_tasks),
    path('userapi/', views.UserApi.as_view()),
    path('taskdelete/<int:id>', views.TaskDelete.as_view(), name='task_delete'),
]
