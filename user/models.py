import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models




def upload_img_file(instance, filename: str) -> str:
    user_id = getattr(instance, 'id', None)
    new_filename = '.'.join((str(uuid.uuid4()), filename.split('.')[1]))

    return f'user/{user_id}/{new_filename}'

# Create your models here.


class User(AbstractUser):
    class RoleEnum(models.TextChoices):
        ADMIN = "ADMIN"
        USER = "USER"
    profile_pic = models.ImageField(upload_to=upload_img_file, null=True)


class UserToken(models.Model):
    token = models.SlugField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)



