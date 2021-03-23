from django.urls import path

from . import views

urlpatterns = [
    path('tasksfilteredbyuser/', views.index),
    path('jsonresponse/', views.snippet_list, name='get'),
    path('taskresponse/', views.snippet_drf, name='get'),
    path('userresponse/', views.user_drf, name='get'),
    path('userclasspaginated/', views.UserList.as_view()),
    path('taskclasspaginated/', views.TaskList.as_view()),
    path('taskapi/', views.TaskAPI.as_view()),
    path('filter/', views.Filter.as_view()),
    path('userapi/', views.UserApi.as_view()),
]
