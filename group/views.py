from django.db.models import Q
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView

from course.models import Course
from group.forms import CheckForm, SearchForm
from group.models import Group
from solution.models import Solution
from task.models import Task1
from user.models import User

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            try:
                tasks_list = Task1.objects.filter(Q(number__exact=query) |
                                               Q(text__icontains=query) |
                                               Q(thema__name__icontains=query))
                courses_list = Course.objects.filter(Q(name__icontains=query) |
                                                Q(price__exact=query))
            except:
                tasks_list = Task1.objects.filter(Q(text__icontains=query) |
                                               Q(thema__name__icontains=query))
                courses_list = Course.objects.filter(Q(name__icontains=query))

            return render(request, "search_list.html", {'task_list': tasks_list,
                                                        'course_list': courses_list })




class GroupListView(ListView):
    model = Group

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseRedirect(reverse('login'))
        else:
            return super().get(self, request, *args, **kwargs)


    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.__contains__('course'):
            course = self.request.GET.__getitem__('course')
            queryset = queryset.filter(course=course)
        return queryset


class GroupDetailView(DetailView):
    model = Group
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseRedirect(reverse('login'))
        else:
            return super().get(self, request, *args, **kwargs)



def stats_stud(request,pk,id):
    group = Group.objects.get(id=pk)
    stud = User.objects.get(id=id)

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if group.kurator != request.user or not request.user.is_staff:
        return HttpResponseRedirect(reverse('index'))
    lessons = group.course.lessons.all()
    tasks = Task1.objects.filter(lesson__in=lessons)

    solutions = Solution.objects.filter(user=stud,task__in=tasks,isTrue=Solution.Right.UNKNOWN)
    CheckFormset = formset_factory(CheckForm, extra=len(solutions))
    if request.method == 'POST':
        formset = CheckFormset(request.POST)
        for i in range(len(solutions)):
            formset[i].prefix = solutions[i].id

        if formset.is_valid():
            for form in formset:
                check = form.cleaned_data['isTrue']
                print(check)
                print(form.getSol().isTrue)
                sol = form.getSol()
                if check =="RIGHT":
                    print("hiii")
                    sol.isTrue = Solution.Right.RIGHT

                else:
                    sol.isTrue = Solution.Right.FALSE
                sol.save()
    else:
        formset = CheckFormset()
        for i in range(len(solutions)):
            formset[i].prefix = solutions[i].id
            print(formset[i].prefix)

        return render(request, 'hi3.html', {'formset': formset})
    return redirect(reverse("index"))





# def check():