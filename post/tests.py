from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from post.models import Post, Comment

###########################################################################################
# NOTE:
# The type of database that using in testing by default is sqlite3 we need to
# ensure that is to comment out all the Postgres stuff in project/.env
# DATABASES should be set to use SQLite
###########################################################################################



# ############### 
# #### just prepare the SETUP 
# ############### 

class PostTests(APITestCase):
    """
    Class to test Post and it's information 
    """
    @classmethod
    def setUpTestData(cls):
        """
        setUpTestData for testing purposes
        """
        # Create a user 
        test_user = get_user_model().objects.create_user(
            email="test@test.com", password="test12345"
        )
        test_user.save()
    
        
        # create a post 
        post = Post.objects.create(
            author = test_user,
            title = 'my first post',
            intro = 'test intro text',
            body = 'test body text',
            image = "http://127.0.0.1:8000/images/test_sICDkeC.png",
        )
        post.save()

        comment = Comment.objects.create(
            post= post,
            author= test_user,
            text= 'test comment'
            )
        comment.save()    

    def setUp(self):
        """ Log in within the above created user  """
        self.client.login(email="test@test.com", password="test12345")

    def test_post_model(self):
        """
        test post model to check the existence data 
        """
        post = Post.objects.get(id=1)
        actual_author = post.author
        actual_title = str(post.title)
        actual_intro = str(post.intro)
        actual_body = str(post.body)
        # actual_slug = str(post.slug)
        actual_image = str(post.image)

        self.assertEqual(actual_author, post.author)
        self.assertEqual(actual_title, post.title)
        self.assertEqual(actual_intro, post.intro)
        self.assertEqual(actual_body, post.body)
        # self.assertEqual(actual_slug, post.slug)
        self.assertEqual(actual_image, post.image)

    def test_comment_model(self):
        """
        test comment model to check the existence data 
        """
        comment = Comment.objects.get(id=1)
        actual_post = comment.post
        actual_author = comment.author
        actual_text = str(comment.text)
        

        self.assertEqual(actual_post, comment.post)
        self.assertEqual(actual_author, comment.author)
        self.assertEqual(actual_text, comment.text)

    def test_get_posts_list(self):
        """
        test get post list using ID existed  
        """
        url = reverse("post_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post = response.data
        self.assertEqual(len(post), 1)

    def test_get_comment_list(self):
        """
        test get comment list using ID existed  
        """
        url = reverse("comment_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        comment = response.data
        self.assertEqual(len(comment), 1)

    def test_create_post(self):
        """
        test create post form sckratch 
        """
        url = reverse("post_list")
        data = {
            'author': 'test_user',
            'title': 'my first post',
            'intro': 'test intro text',
            'body': 'test body text',
            'image': "http://127.0.0.1:8000/images/test_sICDkeC.png",
            }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 400)

        post = Post.objects.all()
        self.assertEqual(len(post), 1)

    def test_create_comment(self):
        """
        test create comment form sckratch 
        """
        url = reverse("comment_list")
        data = {
            'post': 1,
            'author': 1,
            'text': 'test comment'
            }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 201)

        comment = Comment.objects.all()
        self.assertEqual(len(comment), 2)

    def test_delete_post(self):
        """
        test delete post within ID 
        """
        url = reverse("post_details", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        post = Post.objects.all()
        self.assertEqual(len(post), 0)

    def test_delete_comment(self):
        """
        test delete comment within ID 
        """
        url = reverse("comment_details", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        comment = Comment.objects.all()
        self.assertEqual(len(comment), 0)

    def test_update_post(self):
        """
        test update post within ID 
        """
        url = reverse("post_details", args=(1,))
        data = {
            'author': 'test user update',
            'title': 'my first post update',
            'intro': 'test intro text update',
            'body': 'test body text update',
            'image': "http://127.0.0.1:8000/images/test_sICDkeC.png",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 400)

    def test_update_comment(self):
        """
        test update comment within ID 
        """
        url = reverse("comment_details", args=(1,))
        data = {
            'post': 2,
            'author': 2,
            'text': 'test comment updated'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 400)
        
    
