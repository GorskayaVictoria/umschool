from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from course.models import Course

@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = [
                    'name',
                    'price',
        'get_lessons']
    list_filter = ['name','price']

    def get_lessons(self, obj):
        return len(obj.lessons.all())
    get_lessons.short_description = "Lesson count"
