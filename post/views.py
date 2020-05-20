from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView

from comment.forms import CommentForm
from comment.models import CommentPost
from post.forms import PostForm
from post.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.__contains__('thema'):
            thema = self.request.GET.__getitem__('thema')
            queryset = queryset.filter(thema=thema)
        elif self.request.GET.__contains__('author'):
            author = self.request.GET.__getitem__('author')
            queryset = queryset.filter(author=author)
        return queryset

# http://127.0.0.1:8000/tasks/?number=12

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = CommentPost.objects.filter(post=super().get_object())
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        else:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                CommentPost.objects.create(text=comment_form.cleaned_data['text'],
                                               post=super().get_object(),
                                               user=request.user)
                return redirect(reverse("index"))


class PostCreateView(TemplateView):
    template_name = "post/post_create.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseRedirect(reverse('login'))
        else:
            return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        else:
            post_form = PostForm(request.POST, request.FILES)
            if post_form.is_valid():
                post1 = Post.objects.create(author=request.user,text=post_form.cleaned_data['text'],original=post_form.cleaned_data['original'])
                post1.thema.add(*post_form.cleaned_data['thema'])
                print(post_form.cleaned_data["thema"])
                return super().get(self, request, *args, **kwargs)