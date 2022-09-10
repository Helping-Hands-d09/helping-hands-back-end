from django.urls import path

from campaign.views import (
    LocationList,
    LocationDetails,
    CategoryList,
    CategoryDetails,
    CampaignList,
    CampaignDetails,
    # JoinedCampaignList,
    # JoinedCampaignDetails,
)


urlpatterns = [
    path("location/", LocationList.as_view(), name="location_list"),
    path("location/<int:pk>/", LocationDetails.as_view(), name="location_detail"),
    path("category/", CategoryList.as_view(), name="category_list"),
    path("category/<int:pk>/", CategoryDetails.as_view(), name="category_detail"),
    # path("joined-campaign/", JoinedCampaignList.as_view(), name="category_list"),
    # path("joined-campaign/<int:pk>/", JoinedCampaignDetails.as_view(), name="category_detail"),
    path("", CampaignList.as_view(), name="campaign_list"),
    path("<int:pk>/", CampaignDetails.as_view(), name="campaign_detail"),
]