from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from solution.models import Solution



@admin.register(Solution)
class SolutionAdmin(ModelAdmin):
    list_display = ['solution',
                    'task',
                    'isTrue',
                    'user',
                    'date']
    list_filter = ['user','isTrue','task']



