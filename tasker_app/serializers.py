from rest_framework import serializers
from django.contrib.auth.models import Group, User
from .models import Task_todo
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class Task_todoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task_todo
        fields = ('id', 'title', 'description')
