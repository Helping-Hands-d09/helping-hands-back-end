from django.urls import path

from post.views import PostList, PostDetails, CommentList

urlpatterns = [
    
    path('', PostList.as_view() ,name='post_list'),
    path('<int:pk>/', PostDetails.as_view() ,name='post_details'),
    path('comments/', CommentList.as_view() ,name='comment_list'),


]
