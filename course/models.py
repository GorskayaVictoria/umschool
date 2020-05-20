from django.db import models

# Create your models here.
from lesson.models import Lesson


class Course(models.Model):
    lessons = models.ManyToManyField(Lesson,null=True)
    name = models.TextField()
    price = models.IntegerField(default=0)
