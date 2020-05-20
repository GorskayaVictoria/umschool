from django.db import models

# Create your models here.
from django.utils import timezone

from course.models import Course
from post.models import Post
from task.models import Task1
from user.models import User


class Comment(models.Model):
    text = models.TextField()
    task = models.ForeignKey(Task1,on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now)


class CommentPost(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now)


class CommentCourse(models.Model):
    text = models.TextField()
    course = models.ForeignKey(Course,on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now)