from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView

from comment.forms import CommentForm
from comment.models import Comment
from task.models import Task1


class Task1ListView(ListView):
    model = Task1

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.__contains__('number'):
            number = self.request.GET.__getitem__('number')
            queryset = queryset.filter(number=number)
        return queryset

# http://127.0.0.1:8000/tasks/?number=12

class Task1DetailView(DetailView):
    model = Task1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(task=super().get_object())
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        else:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                Comment.objects.create(text=comment_form.cleaned_data['text'],
                                               task=super().get_object(),
                                               user=request.user)
                return redirect(reverse("index"))
