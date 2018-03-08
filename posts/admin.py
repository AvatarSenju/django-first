from django.contrib import admin
from posts.models import Post
# Register your models here.

class PostModel(admin.ModelAdmin):
    list_display=["title","updated","timestamp","title"]
    list_display_links=["title"]
    list_filter=["title"]
admin.site.register(Post,PostModel)
