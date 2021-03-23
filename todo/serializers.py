from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from django.contrib.auth.models import User

from todo.models import Task

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['username']
        fields = "__all__"
        extra_kwargs = {
            'username': {'validators': []},
             'slug_field' : 'username'
        }



class taskSerializer(serializers.ModelSerializer):
    assigned_user = userSerializer(read_only=True )
    #assigned = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Task
        #fields = ['id', 'title', 'created','assigned']
        fields = "__all__"
        #def to_representation(self, instance):
         #   self.fields['assigned'] = userSerializer(read_only=True)
          #  return super(taskSerializer, self).to_representation(instance)
        #validators = []

       # def create(self, validated_data):
            #order = Task.objects.get(pk=validated_data.pop('event'))
        #    instance = Task.objects.create(**validated_data)
            #Assignment.objects.create(Order=order, Equipment=instance)
         #   return instance

        #def to_representation(self, instance):
         #   representation = super(taskSerializer, self).to_representation(instance)
            #representation['assigment'] = AssignmentSerializer(instance.assigment_set.all(), many=True).data
          #  return representation

            # extra_kwargs = {
        #    'id': {'read_only': True},
         #  'assigned.username': {'validators': []},
        #}

        #fields = '__all__'