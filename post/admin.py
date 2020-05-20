from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from post.models import Post

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ['author',
                    'original',
                    'text',
                    'get_thema']
    list_filter = ['author']

    def get_thema(self, obj):
        return len(obj.thema.all())
    get_thema.short_description = "Thema count"
