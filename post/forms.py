from django.forms import forms, modelformset_factory, BaseModelFormSet, ModelForm
from django import forms

from post.models import Post
from solution.models import Solution
from task.models import Task1
import random




class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['original', 'text','thema']






