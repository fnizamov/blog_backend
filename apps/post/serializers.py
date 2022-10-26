from dataclasses import fields
from email.policy import default
from requests import request
from rest_framework import serializers
from django.db.models import Avg
from .models import(
    Post,
    Rating,
    Tag,
    Comment
)

class PostListSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Post
        fields = ('user', 'title', 'image', 'slug')


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')    

    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comments'] = CommentSerializer(
            instance.comments.all(), many=True
        ).data
        rating = instance.ratings.aggregate(Avg('rating'))['rating__avg']
        if rating:
            representation['rating'] = round(rating, 1)
        else:
            representation['rating'] = 0.0
        return representation


class PostCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault(),
        source='user.username'
    )

    class Meta:
        model = Post
        fields = '__all__'
    

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault(),
        source='user.username'
    )

    class Meta:
        model = Comment
        exclude = ['post']


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.username'
    )
    
    class Meta:
        model = Rating
        fields = ('rating', 'user', 'post')
        
    def validate(self, attrs):
        user = self.context.get('request').user
        attrs['user'] = user
        rating = attrs.get('rating')
        if rating not in (1, 2, 3, 4, 5):
            raise serializers.ValidationError('Wrong value! Rating must be between from 1 to 5'
            )
        return attrs

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating')
        return super().update(instance, validated_data)