from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from group.models import Group

@admin.register(Group)
class GroupAdmin(ModelAdmin):
    list_display = ['kurator',
                    'course',
                    'get_studs']
    list_filter = ['kurator','course__name']

    def get_studs(self, obj):
        return len(obj.students.all())
    get_studs.short_description = "Studs count"