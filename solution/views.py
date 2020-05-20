from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from solution.forms import SolutionForm
from solution.models import Solution
from task.models import Task1



def task(request,pk):
    task = Task1.objects.filter(number=pk)
    SolutionFormSet = formset_factory(SolutionForm, extra=len(task))
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        formset = SolutionFormSet(request.POST,request.FILES)
        for i in range(len(task)):
            formset[i].prefix = task[i].id
            print(formset[i].prefix)
        print(formset)
        if formset.is_valid():
            for form in formset:
                sol = form.cleaned_data['solution']
                print(sol)
                # print(Solution.objects.get(user=request.user,task=form.getTask()))
                # if solution!=None:
                #     solution.solution=sol
                #     solution.isTrue=solution.isRight()
                #     solution.save()
                # else:
                if form.getTask().number>23:
                    Solution.objects.create(solution=sol,task=form.getTask(),user=request.user,isTrue=Solution.Right.UNKNOWN,profile_pic=form.cleaned_data["profile_pic"])

                else:
                    Solution.objects.create(solution=sol,task=form.getTask(),user=request.user,isTrue=(sol==form.getTask().answer))

    else:
        formset = SolutionFormSet()
        for i in range(len(task)):
            formset[i].prefix = task[i].id
            print(formset[i].prefix)

        return render(request, 'hi.html', {'formset': formset})
    return redirect(reverse("index"))



def varik(request):
    SolutionFormSet = formset_factory(SolutionForm, extra=27)
    if request.method == 'POST':
        formset = SolutionFormSet(request.POST)
        for i in range(27):
            formset[i].prefix = i+1
            print(formset[i].prefix)
        print(formset)
        if formset.is_valid():
            for form in formset:
                try:
                    sol = form.cleaned_data['solution']
                    print(sol)
                    if form.getTask().number > 23:
                        Solution.objects.create(solution=sol, task=form.getTask(), user=request.user,
                                                isTrue=(sol == form.getTask().answer),
                                                profile_pic=form.cleaned_data["profile_pic"])

                    else:
                        Solution.objects.create(solution=sol, task=form.getTask(), user=request.user,
                                                isTrue=(sol == form.getTask().answer))
                except:
                    pass
    else:
        formset = SolutionFormSet()
        for i in range(27):
            formset[i].prefix = i+1
            print(formset[i].prefix)

        return render(request, 'h2i.html', {'formset': formset})
    return redirect(reverse("index"))