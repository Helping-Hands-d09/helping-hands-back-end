from rest_framework import serializers 
from django.contrib.auth import get_user_model

from post.models import Post, Comment
from accounts.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    """ This serializer is used to serialize a post object into a JSON file """
    class Meta: 
        model = Post
        fields = ('author', 'title', 'intro', 'body', 'image') 


class CommentSerializer(serializers.ModelSerializer):
    """ This serializer is used to serialize a comment object into a JSON file"""
    class Meta: 
        model = Comment
        fields = '__all__' 
        # depth = 1

class CommentsOfPostSerializer(serializers.ModelSerializer):
    """ This serializer is used to serialize a comment object into a JSON file"""
    author = UserSerializer(read_only = True) 
    author_data = serializers.PrimaryKeyRelatedField(queryset = get_user_model().objects.all(), source = "member", write_only=True)
    
    class Meta: 
        model = Comment
        fields = '__all__' 
        # depth = 1