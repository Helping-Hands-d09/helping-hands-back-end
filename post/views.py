from rest_framework.generics  import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from post.models import Post, Comment
from post.serializers import PostSerializer, CommentSerializer


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetails(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 



class CommentList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 