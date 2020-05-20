from django.forms import forms, modelformset_factory, BaseModelFormSet
from django import forms
from solution.models import Solution
from task.models import Task1
import random


CHOICES =(
    ("RIGHT", "True"),
    ("FALSE", "False"),
)

class CheckForm(forms.Form):
    isTrue = forms.ChoiceField(choices=CHOICES)


    def getSol(self):
        return Solution.objects.get(id=self.prefix)

class SearchForm(forms.Form):
    query = forms.CharField()



