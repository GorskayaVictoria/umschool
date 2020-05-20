from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from user.models import User

@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ['username',
                    'first_name',
                    'last_name',
                    'email',
                    'is_staff']
    list_filter = ['is_staff']


