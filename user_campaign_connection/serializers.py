from rest_framework import serializers 
from django.contrib.auth import get_user_model
from campaign.models import Campaign

from user_campaign_connection.models import JoinedCampaign
from campaign.models import Campaign

from accounts.serializers import UserSerializer
from campaign.serializers import CampaignSerializer


class JoinedCampaignSerializer(serializers.ModelSerializer):
    member = UserSerializer(read_only = True) 
    campaign = CampaignSerializer(read_only = True)

    member_data = serializers.PrimaryKeyRelatedField(queryset = get_user_model().objects.all(), source = "member", write_only=True)
    campaign_data = serializers.PrimaryKeyRelatedField(queryset = Campaign.objects.all(), source = "campaign", write_only=True)

    class Meta: 
        model = JoinedCampaign 
        fields = "__all__"