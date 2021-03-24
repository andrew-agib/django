from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DeleteView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from todo.models import Task
from todo.serializers import TaskSerializer, UserSerializer
from .filters import TaskFilter


@csrf_exempt
def tasks_get(request):
    if request.method == 'GET':
        snippets = Task.objects.all()
        serializer = TaskSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def filtered_tasks(request):
    num_tasks = Task.objects.filter(assigned_to=request.user)
    context = {
        'num_tasks': num_tasks,
    }
    return render(request, 'todo/tasks.html', context=context)


@api_view(['GET', 'POST'])
def tasks_drf(request):
    if request.method == 'GET':
        snippets = Task.objects.all()
        serializer = TaskSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def user_drf(request):
    if request.method == 'GET':
        snippets = User.objects.all()
        snippets = Paginator(snippets, 3)
        snippets = snippets.page(1)
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserList(generic.ListView):
    model = User
    template_name = 'user_list.html'
    paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        num_users = super().get_context_data(**kwargs)
        context = {
            'num_users': num_users,
        }
        return context


class TaskList(generic.ListView):
    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)

    model = Task
    template_name = 'task_list.html'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        num_tasks = super().get_context_data(**kwargs)
        context = {
            'num_tasks': num_tasks,
        }
        return context


class TaskAPI(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(title=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Filter(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        assigned_to = self.kwargs['assigned_to']
        return Task.objects.filter(task__assigned_to=assigned_to)


def search_tasks(request):
    task_list = Task.objects.all()
    task_filter = TaskFilter(request.GET, queryset=task_list)
    return render(request, 'filter.html', {'filter': task_filter})


class UserApi(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskDelete(DeleteView):
    model = Task
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = 'task_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task_api')
