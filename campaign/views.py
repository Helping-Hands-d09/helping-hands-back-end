from rest_framework.generics  import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from campaign.models import Campaign, Location, Category, JoinedCampaign
from campaign.serializers import CampaignSerializer, CategorySerializer, LocationSerializer, JoinedCampaignSerializer
from utils.permissions import IsAdminUserOrReadOnly, IsOwnerOrReadOnly 



class LocationList(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer  

class LocationDetails(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all() 
    serializer_class = LocationSerializer 
    permission_classes = (IsAdminUserOrReadOnly,)




class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  

class CategoryDetails(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer 
    permission_classes = (IsAdminUserOrReadOnly,)


class CampaignList(ListCreateAPIView):
    serializer_class = CampaignSerializer
    def get_queryset(self):
        queryset = Campaign.objects.all() 
        organizer = self.request.query_params.get('organizer') 
        if organizer is not None: 
            queryset = Campaign.objects.filter(organizer=organizer)
        return queryset 


class CampaignDetails(RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all() 
    serializer_class = CampaignSerializer 
    permission_classes = (IsOwnerOrReadOnly,)


class JoinedCampaignList(ListCreateAPIView):
    queryset = JoinedCampaign.objects.all()
    serializer_class = JoinedCampaignSerializer  

class JoinedCampaignDetails(RetrieveUpdateDestroyAPIView):
    queryset = JoinedCampaign.objects.all() 
    serializer_class = JoinedCampaignSerializer 
    # permission_classes = (IsAdminUserOrReadOnly,)

