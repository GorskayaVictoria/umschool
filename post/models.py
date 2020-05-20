from django.db import models

# Create your models here.
from task.models import Thema
from user.models import User


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    original = models.URLField(null=True)
    thema = models.ManyToManyField(Thema,null=True)
    text = models.TextField()