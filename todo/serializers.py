from django.contrib.auth.models import User
from rest_framework import serializers

from todo.models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "last_name"]


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['title', 'assigned_to', 'description']

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)
        # fields = "__all__"
