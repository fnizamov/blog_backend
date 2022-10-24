from dataclasses import fields
from requests import request
from rest_framework import serializers
from .models import(
    Post,
    Tag,
    Comment
)

class PostListSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Post
        fields = ('user', 'title', 'image')


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')    

    class Meta:
        model = Post
        fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()

    class Meta:
        model = Post
        exclude = ['user']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['id']
        