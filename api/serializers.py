from rest_framework import serializers

from post.models import Post
from task.models import Task1


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('author', 'original', 'text', 'thema')

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task1
        fields = ('number', 'text', 'part', 'thema','answer')
