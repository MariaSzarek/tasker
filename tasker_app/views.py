from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from .models import Task_todo
from .serializers import UserSerializer, Task_todoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class Task_todoView(viewsets.ModelViewSet):
    queryset = Task_todo.objects.all()
    serializer_class = Task_todoSerializer

    # def get_object(self):
    #     task_id = self.kwargs['pk']
    #     return Task_todo.objects.get(pk=task_id)
