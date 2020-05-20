from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from comment.models import Comment, CommentPost, CommentCourse



@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ['text',
                    'task',
                    'user',
                    'date']
    list_filter = ['user', 'task__number']

    date_hierarchy = 'date'

    def get_post(self, obj):
        return obj.post.name
    get_post.short_description = "Task1"
    get_post.admin_order_field = "task__name"


@admin.register(CommentPost)
class CommentAdmin(ModelAdmin):
    list_display = ['text',
                    'post',
                    'user',
                    'date']
    list_filter = ['user','post__thema__name']

    date_hierarchy = 'date'

    def get_post(self, obj):
        return obj.post.name
    get_post.short_description = "Post"
    get_post.admin_order_field = "post__name"


@admin.register(CommentCourse)
class CommentAdmin(ModelAdmin):
    list_display = ['text',
                    'course',
                    'user',
                    'date']
    list_filter = ['user', 'course__name']

    date_hierarchy = 'date'

    def get_post(self, obj):
        return obj.post.name
    get_post.short_description = "Course"
    get_post.admin_order_field = "course__name"