from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
   #path('', views.snippet_drf, name='get'),
    #path('', views.snippet_drf, name='POST'),
    path('', views.user_drf, name='get'),
    #path('', views.UserListView ),
    #path('', views.UserPost),
   #path('', views.EquipmentSetList.as_view()),
    #path('', views.TaskDeleteVIew.as_view()),

   path('', views.UserList.as_view()),

    #path('', views.user_drf, name='POST'),
    #path('', views.index),
   #path('', views.snippet_list, name='get')

]