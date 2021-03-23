from django.contrib.auth.models import User
from rest_framework import serializers

from todo.models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
        extra_kwargs = {
            'username': {'validators': []},
            'slug_field': 'username'
        }


class TaskSerializer(serializers.ModelSerializer):
    assigned_user = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"

