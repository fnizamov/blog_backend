from django.contrib import admin
from .models import Like, Post, Rating, Tag, PostImage

admin.site.register((Post, Tag, Rating, PostImage, Like))

