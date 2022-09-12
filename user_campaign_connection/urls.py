from django.urls import path


from user_campaign_connection.views import (
    ConnectionList,
    ConnectionDetails,
    CreatedCampaignFilter,
    JoinedCampaignFilter,
)

urlpatterns = [
    path("", ConnectionList.as_view(), name="connection_list"),
    path("<int:pk>/", ConnectionDetails.as_view(), name="connection_detail"),
    path('campaign-members/<slug:id>', JoinedCampaignFilter.as_view(), name="members_list"),
    path('member-campaigns/<slug:id>', CreatedCampaignFilter.as_view(), name="campaigns_list"),
    
]


