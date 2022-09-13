from rest_framework.generics  import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from user_campaign_connection.models import JoinedTables
from user_campaign_connection.serializers import ConnectionSerializer, JoinedCampaignSerializer, CreatedCampaignSerializer
from utils.permissions import IsAdminUserOrReadOnly, IsOwnerOrReadOnly 



class ConnectionList(ListCreateAPIView):
    queryset = JoinedTables.objects.all()
    serializer_class = ConnectionSerializer  

class ConnectionDetails(RetrieveUpdateDestroyAPIView):
    queryset = JoinedTables.objects.all() 
    serializer_class = ConnectionSerializer 
    # permission_classes = (IsAdminUserOrReadOnly,)

class CreatedCampaignFilter(ListCreateAPIView):
    serializer_class = CreatedCampaignSerializer

    def get_queryset(self):
        member_id = self.request.query_params.get('id', 0)
        print(member_id)
        return JoinedTables.objects.filter(member=member_id)

class JoinedCampaignFilter(ListCreateAPIView):
    serializer_class = JoinedCampaignSerializer

    def get_queryset(self):
        campaign_id = self.request.query_params.get('id', 0)
        print(campaign_id)
        return JoinedTables.objects.filter(campaign=campaign_id)
