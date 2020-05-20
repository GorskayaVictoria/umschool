from django.forms import forms, modelformset_factory, BaseModelFormSet
from django import forms
from solution.models import Solution
from task.models import Task1
import random

class CommentForm(forms.Form):
    text = forms.CharField()






