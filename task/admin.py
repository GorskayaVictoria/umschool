from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from task.models import Task1, Thema

@admin.register(Task1)
class Task1Admin(ModelAdmin):

    list_display = ['answer',
                    'number',
                    'text',
                    'part',
                    'thema']
    list_filter = ['number','part','thema']


@admin.register(Thema)
class ThemaAdmin(ModelAdmin):
    list_display = ['name',
                    'complexity']
    list_filter = ['name']


