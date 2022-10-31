from django.contrib import admin
from .models import Like, Post, Rating, Tag, PostImage

admin.site.register((Tag, Rating, Like))


class TabularInLineImages(admin.TabularInline):
    model = PostImage
    extra = 3
    fields = ['image']


class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [TabularInLineImages]

admin.site.register(Post, PostAdmin)