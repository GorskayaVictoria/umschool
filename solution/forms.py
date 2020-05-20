from django.forms import forms, modelformset_factory, BaseModelFormSet
from django import forms
from solution.models import Solution
from task.models import Task1
import random

class SolutionForm(forms.Form):
    solution = forms.CharField()
    profile_pic = forms.FileField(required=False)

    def getTask(self):
        return Task1.objects.get(id=self.prefix)

    def getVar(self):
        tasks = list(Task1.objects.filter(number=self.prefix))
        return random.choice(tasks) if tasks else None




