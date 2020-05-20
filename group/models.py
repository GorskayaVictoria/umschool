from django.db import models

# Create your models here.
from course.models import Course
from user.models import User


class Group(models.Model):
    kurator = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(User,null=True,related_name="student")