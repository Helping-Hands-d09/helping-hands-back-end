from rest_framework import serializers 
from django.contrib.auth import get_user_model

from campaign.models import Campaign, Location, Category 
from accounts.serializers import UserSerializer 


class LocationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Location 
        fields = '__all__' 


class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category 
        fields = '__all__' 

class CampaignSerializer(serializers.ModelSerializer):
    organizer = UserSerializer(read_only = True) 
    category = CategorySerializer(read_only = True)
    location = LocationSerializer(read_only = True) 

    organizer_name = serializers.PrimaryKeyRelatedField(queryset = get_user_model().objects.all(), source = "organizer", write_only=True)
    category_name  = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all(), source = "category", write_only=True)
    location_name = serializers.PrimaryKeyRelatedField(queryset = Location.objects.all(), source = "location", write_only=True)
        
    class Meta: 
        model = Campaign 
        fields = '__all__' 
