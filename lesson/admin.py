from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from lesson.models import Lesson

@admin.register(Lesson)
class LessonAdmin(ModelAdmin):
    list_display = ['name',
                    'video',
                    'get_tasks',
                    'get_thema',
                    'get_posts',
                    'get_users']
    list_filter = ['name']

    def get_tasks(self, obj):
        return len(obj.task.all())

    def get_thema(self, obj):
        return len(obj.thema.all())

    def get_posts(self, obj):
        return len(obj.posts.all())

    def get_users(self, obj):
        return len(obj.user.all())

    get_tasks.short_description = "Tasks count"
    get_thema.short_description = "Thema count"
    get_posts.short_description = "Posts count"
    get_users.short_description = "Studs count"