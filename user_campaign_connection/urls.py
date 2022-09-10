from django.urls import path

from user_campaign_connection.views import (
    JoinedCampaignList,
    JoinedCampaignDetails,
)


urlpatterns = [
    path("joined-campaign/", JoinedCampaignList.as_view(), name="category_list"),
    path("joined-campaign/<int:pk>/", JoinedCampaignDetails.as_view(), name="category_detail"),
    
]