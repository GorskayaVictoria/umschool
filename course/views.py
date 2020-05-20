from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView

from comment.forms import CommentForm
from comment.models import CommentCourse
from course.models import Course


class CourseListView(ListView):
    model = Course


# http://127.0.0.1:8000/tasks/?number=12

class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = CommentCourse.objects.filter(course=super().get_object())
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        else:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                CommentCourse.objects.create(text=comment_form.cleaned_data['text'],
                                               course=super().get_object(),
                                               user=request.user)
                return redirect(reverse("index"))