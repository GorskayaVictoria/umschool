from django.db import models

# Create your models here.

class Thema(models.Model):

    class Complexity(models.TextChoices):
        LIGHT = "LIGHT"
        MIDDLE = "MIDDLE"
        HARD = "HARD"

    name = models.TextField()
    complexity = models.CharField(choices=Complexity.choices,default=Complexity.MIDDLE,max_length=255)

class Task1(models.Model):

    class Part(models.TextChoices):
        FIRST = 1
        SECOND = 2


    answer = models.TextField()
    number = models.IntegerField()
    text = models.TextField()
    part = models.CharField(choices=Part.choices,default=Part.FIRST,max_length=255)
    thema = models.ForeignKey(Thema, on_delete=models.SET_NULL, null=True,default=None)



