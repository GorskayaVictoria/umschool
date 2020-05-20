from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView, ListView

from lesson.models import Lesson
from solution.forms import SolutionForm
from solution.models import Solution
from task.models import Task1




class LessonListView(ListView):
    model = Lesson

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.__contains__('thema'):
            thema = self.request.GET.__getitem__('thema')
            queryset = queryset.filter(thema=thema)
        return queryset

# http://127.0.0.1:8000/tasks/?number=12

class LessonDetailView(DetailView):
    model = Lesson


def task(request,pk):
    lesson = Lesson.objects.get(id=pk)
    task = Task1.objects.filter(lesson=lesson)
    SolutionFormSet = formset_factory(SolutionForm, extra=len(task))
    stud = request.user

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        formset = SolutionFormSet(request.POST,request.FILES)
        for i in range(len(task)):
            formset[i].prefix = task[i].id
        if formset.is_valid():
            for form in formset:
                sol = form.cleaned_data['solution']
                if form.getTask().number>23:
                    Solution.objects.create(solution=sol,task=form.getTask(),user=request.user,isTrue=(sol==form.getTask().answer),profile_pic=form.cleaned_data["profile_pic"])

                else:
                    Solution.objects.create(solution=sol,task=form.getTask(),user=request.user,isTrue=(sol==form.getTask().answer))
            stud.lesson_set.add(lesson)

    else:
        if stud in (lesson.user.all()):
            return redirect(reverse("index"))
        formset = SolutionFormSet()
        for i in range(len(task)):
            formset[i].prefix = task[i].id
        return render(request, 'lesson/test_lesson.html', {'formset': formset, 'lesson':lesson})
    return redirect(reverse("index"))