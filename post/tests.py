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
            slug = 'my-first-post' ,
            image = "http://127.0.0.1:8000/images/test_sICDkeC.png",
        )
        post.save()

        comment = Comment.objects.create(
            post= 1 ,
            author= 1 ,
            text= 'test comment'
            )
        comment.save()    

    def setUp(self):
        """ Log in within the above created user  """
        self.client.login(email="test@test.com", password="test12345")
