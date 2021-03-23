from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics

from todo.models import Task
from todo.serializers import taskSerializer, userSerializer


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Task.objects.all()
        serializer = taskSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = taskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def index(request):
    # num_tasks = Task.objects.all().values
    num_tasks = Task.objects.filter(assigned=request.user).filter(title='sd')
    #num_tasks = Task.objects.filter(assigned=request.user).filter(title='sd')

    field_name = 'title'
    obj = Task.objects.first()
    field_object = Task._meta.get_field(field_name)
    field_value = field_object.value_from_object(obj)
    # num_tasks = Task.objects.filter(task_finished=True)
    context = {
        'num_tasks': num_tasks,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'todo/tasks.html', context=context)


@api_view(['GET', 'POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def snippet_drf(request):
    if request.method == 'GET':
        snippets = Task.objects.all()
        serializer = taskSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # def perform_update(self, serializer):
        #    user = self.request.user
        #   userid = str(user.id)
        #  serializer.save(assigned=userid)
        # data = JSONParser().parse(request)
        # print(data)
        # serializer = taskSerializer(data=data)
        # if serializer.is_valid():
        #   serializer.save()
        #  return Response(serializer.data, status=201)
        # return Response(serializer.errors, status=404)
        serializer = taskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def user_drf(request):
    if request.method == 'GET':
        snippets = User.objects.all()
        snippets = Paginator(snippets, 3)
        snippets = snippets.page(1)
        serializer = userSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = userSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class serList(generic.ListView):
    model = User
    template_name = 'user_list.html'
    paginate_by = 1  # if pagination is desired

    def get_context_data(self, *args, **kwargs):
        num_tasks = super().get_context_data(**kwargs)

        # num_tasks = super(UserListView, self).get_queryset(*args, **kwargs)
        # num_tasks ="wdwefde"
        # context['now'] = timezone.now()

        context = {
            'num_tasks': num_tasks,
        }
        # Render the HTML template index.html with the data in the context variable
        return context
    # context_object_name = 'my_book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war


class serList(generic.ListView):
    # solution : https://stackoverflow.com/questions/38471260/django-filtering-by-user-id-in-class-based-listview
    def get_queryset(self):
        return Task.objects.filter(assigned=self.request.user)

    model = Task
    template_name = 'user_list.html'
    paginate_by = 3  # if pagination is desired

    def get_context_data(self, *args, **kwargs):
        num_tasks = super().get_context_data(**kwargs)

        # num_tasks = super(UserListView, self).get_queryset(*args, **kwargs)
        # num_tasks ="wdwefde"
        # context['now'] = timezone.now()

        context = {
            'num_tasks': num_tasks,
        }
        # Render the HTML template index.html with the data in the context variable
        return context


class serList(generic.ListView):
    # solution : https://stackoverflow.com/questions/38471260/django-filtering-by-user-id-in-class-based-listview

    model = Task
    template_name = 'user_list.html'
    paginate_by = 1  # if pagination is desired

    def get_context_data(self, *args, **kwargs):
        num_tasks = super().get_context_data(**kwargs)

        # num_tasks = super(UserListView, self).get_queryset(*args, **kwargs)
        # num_tasks ="wdwefde"
        # context['now'] = timezone.now()

        context = {
            'num_tasks': num_tasks,
        }
        # Render the HTML template index.html with the data in the context variable
        return context





class serList(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = taskSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = taskSerializer


class serList(generics.ListCreateAPIView):
    def perform_update(self, serializer):
        # Save with the new value for the target model fields
        user = self.request.user
        userid = str(user.id)
        serializer.save(stu_assigned=userid)

    queryset = Task.objects.all()
    serializer_class = taskSerializer


class TaskDeleteVIew(generic.DeleteView):
    model = Task
    template_name = 'task_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('list')

    # Render the HTML template index.html with the data in the context variable
