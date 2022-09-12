from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from campaign.models import Campaign, Category, Location
from .models import JoinedTables

###########################################################################################
# NOTE:
# The type of database that using in testing by default is sqlite3 we need to
# ensure that is to comment out all the Postgres stuff in project/.env
# DATABASES should be set to use SQLite
###########################################################################################


class ConnectionTableTests(APITestCase):
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

        connection_table_model = JoinedTables.objects.create(
            campaign = campaign_model,
            member = test_user,
        )

    def setUp(self):
        """ Log in within the above created user  """
        self.client.login(email="test@test.com", password="test12345")


    def test_connection_table_model(self):
        """
        test connection table model to check the existence data 
        """
        connection_table = JoinedTables.objects.get(id=1)
        actual_title = str(connection_table)

        self.assertEqual(actual_title, f"connection c_id{connection_table.campaign} m_id{connection_table.member}")
        

    def test_get_connection_table_list(self):
        """
        test get connection table list using ID existed  
        """
        url = reverse("connection_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        connections = response.data
        self.assertEqual(len(connections), 1)
        

    def test_create_connection_table(self):
        """
        test create connection form sckratch 
        """
        url = reverse("connection_list")
        data = {
            "campaign": 1,
            "member": 1
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 201)

        connections = JoinedTables.objects.all()
        self.assertEqual(len(connections), 2)

    def test_delete_connection_table(self):
        """
        test delete connection within ID 
        """
        url = reverse("connection_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        connections = JoinedTables.objects.all()
        self.assertEqual(len(connections), 0)

    def test_update_connection_table(self):
        """
        test update connection within ID 
        """
        url = reverse("connection_detail", args=(1,))
        data = {
            "campaign": 1,
            "member": 2
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 400)
        connections = JoinedTables.objects.get(id=1)
        self.assertEqual(str(connections), f"connection c_id{connections.campaign} m_id{connections.member}")


