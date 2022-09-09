from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Campaign, Category, Location

###########################################################################################
# NOTE:
# The type of database that using in testing by default is sqlite3 we need to
# ensure that is to comment out all the Postgres stuff in project/.env
# DATABASES should be set to use SQLite
###########################################################################################


class CampiagnTests(APITestCase):
    """
    Class to test campaign and it's information 
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
        
        # create a category  
        category = Category.objects.create(
            title='cleaning'
            )
        category.save()

        # create a location 
        location = Location.objects.create(
            city_name='Amman'
            )
        location.save()
        
        # create a campaign 
        campaign_model = Campaign.objects.create(
            title = "clean world",
            description = 'This campaign aims to clean the streets"',
            date = '2022-09-29',
            organizer = test_user,
            category = category ,
            location = location ,
            available_sets = 25,
            image = "http://127.0.0.1:8000/images/test_sICDkeC.png",
        )
        campaign_model.save()

    def setUp(self):
        """ Log in within the above created user  """
        self.client.login(email="test@test.com", password="test12345")

    def test_campaign_model(self):
        """
        test campaign model to check the existence data 
        """
        campaign = Campaign.objects.get(id=1)
        actual_title = str(campaign.title)
        actual_description = str(campaign.description)
        actual_date = campaign.date
        actual_organizer = campaign.organizer
        actual_category = campaign.category
        actual_location = campaign.location
        actual_available_sets = campaign.available_sets
        actual_image = str(campaign.image)
        self.assertEqual(actual_title, campaign.title)
        self.assertEqual(actual_description, campaign.description)
        self.assertEqual(actual_date, campaign.date)
        self.assertEqual(actual_organizer, campaign.organizer)
        self.assertEqual(actual_category, campaign.category)
        self.assertEqual(actual_location, campaign.location)
        self.assertEqual(actual_available_sets, campaign.available_sets)
        self.assertEqual(actual_image, campaign.image)

    def test_get_campaign_list(self):
        """
        test get campaign list using ID existed  
        """
        url = reverse("campaign_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        campaign = response.data
        self.assertEqual(len(campaign), 1)
        

    def test_create_campaign(self):
        """
        test create campaign form sckratch 
        """
        url = reverse("campaign_list")
        data = {
            'title': "clean world",
            'description': 'This campaign aims to clean the streets"',
            'date': '2022-09-29',
            'organizer': 1,
            'category': 1 ,
            'location': 1 ,
            'available_sets' : 25,
            'image': "http://127.0.0.1:8000/images/test_sICDkeC.png"
            }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 400)

        campaign = Campaign.objects.all()
        self.assertEqual(len(campaign), 1)

    def test_delete_campaign(self):
        """
        test delete campaign within ID 
        """
        url = reverse("campaign_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        campaign = Campaign.objects.all()
        self.assertEqual(len(campaign), 0)

    def test_update_campaign(self):
        """
        test update campaign within ID 
        """
        url = reverse("campaign_detail", args=(1,))
        data = {
            'title': "clean world updated",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 400)
        campaign = Campaign.objects.get(id=1)
        self.assertEqual(campaign.title, "clean world")

    def test_authentication_required(self):
        """
        test authentication and logout functionality 
        """
        self.client.logout()
        url = reverse("campaign_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)



