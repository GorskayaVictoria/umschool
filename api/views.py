from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.permissions import BaseCustomPermission
from api.serializers import PostSerializer, TaskSerializer
from post.models import Post
from task.models import Task1


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [BaseCustomPermission]
    queryset = Task1.objects.all()
    serializer_class = TaskSerializer
