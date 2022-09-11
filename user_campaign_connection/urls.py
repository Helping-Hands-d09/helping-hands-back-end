from django.urls import path

from user_campaign_connection.views import (
    ConnectionList,
    ConnectionDetails,
    CreatedCampaignFilter,
    JoinedCampaignFilter,
)


urlpatterns = [
    path("/", ConnectionList.as_view(), name="category_list"),
    path("/<int:pk>/", ConnectionDetails.as_view(), name="category_detail"),
    path('joined-campaign/<slug:slug>', JoinedCampaignFilter.as_view()),
    path('created-campaign/<slug:slug>', CreatedCampaignFilter.as_view()),
    
]