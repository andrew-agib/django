import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Task
        fields = ['title']
