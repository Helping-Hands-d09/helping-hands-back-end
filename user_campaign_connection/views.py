from rest_framework.generics  import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from user_campaign_connection.models import JoinedCampaign
from user_campaign_connection.serializers import JoinedCampaignSerializer
from utils.permissions import IsAdminUserOrReadOnly, IsOwnerOrReadOnly 



class JoinedCampaignList(ListCreateAPIView):
    queryset = JoinedCampaign.objects.all()
    serializer_class = JoinedCampaignSerializer  

class JoinedCampaignDetails(RetrieveUpdateDestroyAPIView):
    queryset = JoinedCampaign.objects.all() 
    serializer_class = JoinedCampaignSerializer 
    # permission_classes = (IsAdminUserOrReadOnly,)
