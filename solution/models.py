import uuid

from django.utils import timezone
from django.db import models

# Create your models here.
from task.models import Task1
from user.models import User

def upload_img_file(instance, filename: str) -> str:
    user_id = getattr(instance, 'id', None)
    new_filename = '.'.join((str(uuid.uuid4()), filename.split('.')[1]))
    return f'solution/{user_id}/{new_filename}'

class Solution(models.Model):
    class Part(models.TextChoices):
        FIRST = 1
        SECOND = 2

    class Right(models.TextChoices):
        RIGHT = True
        FALSE = False
        UNKNOWN = "UNKNOWN"


    solution = models.TextField(default=None,null=True)
    task = models.ForeignKey(Task1,on_delete=models.SET_NULL, null=True)
    isTrue = models.CharField(choices=Right.choices,default=Right.UNKNOWN,max_length=255)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now)
    profile_pic = models.ImageField(upload_to=upload_img_file, null=True)



