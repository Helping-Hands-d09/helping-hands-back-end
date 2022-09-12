from rest_framework import serializers 
from post.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    """ This serializer is used to serialize a post object into a JSON file """
    class Meta: 
        model = Post
        fields = '__all__' 


class CommentSerializer(serializers.ModelSerializer):
    """ This serializer is used to serialize a comment object into a JSON file"""
    class Meta: 
        model = Comment
        fields = '__all__' 
        # depth = 1