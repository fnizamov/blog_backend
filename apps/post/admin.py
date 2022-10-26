from django.contrib import admin
from .models import Post, Rating, Tag

admin.site.register((Post, Tag, Rating))

