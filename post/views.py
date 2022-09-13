from rest_framework.generics  import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from post.models import Post, Comment
from post.serializers import PostSerializer, CommentSerializer, CommentsOfPostSerializer


class PostList(ListCreateAPIView):
    """ This class represents a list of posts"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetails(RetrieveUpdateDestroyAPIView):
    """ This class represents a details for specific post"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer 

class CommentList(ListCreateAPIView):
    """ This class represents a list of comments"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 


class CommentDetails (RetrieveUpdateDestroyAPIView):
    """This class represents a comment details for specific commment"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 

class CommentsDetailsFliter(ListCreateAPIView):
    """ This class represents a list of comments for specific post using (slug container) """
    serializer_class = CommentsOfPostSerializer

    def get_queryset(self):
        """ override get_queryset to return a list of comments details for specific post """
        post_id = self.request.query_params.get('slug', None)
        return Comment.objects.filter(post=post_id)