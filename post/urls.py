from django.urls import path

from post.views import PostList, PostDetails, CommentList, CommentDetails, CommentsDetailsFliter

urlpatterns = [

    # views for all posts
    path('', PostList.as_view() ,name='post_list'),  

    # views for specific post
    path('<int:pk>/', PostDetails.as_view() ,name='post_details'), 

    # views for all comments for specific post
    path('postcomment/<slug:slug>/', CommentsDetailsFliter.as_view() ,name='comments_details_fliter'), 

    # views for all comments
    path('comments/', CommentList.as_view() ,name='comment_list'),  

    # views for specific comment 
    path('comments/<int:pk>/', CommentDetails.as_view() ,name='comment_details'),


]
