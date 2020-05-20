from django.db import models

# Create your models here.
from post.models import Post
from task.models import Task1, Thema
from user.models import User


class Lesson(models.Model):
    posts = models.ManyToManyField(Post, null=True)
    video = models.URLField()
    task = models.ManyToManyField(Task1, null=True)
    thema = models.ManyToManyField(Thema,null=True)
    name = models.TextField(default="Без названия")
    user = models.ManyToManyField(User, null=True)