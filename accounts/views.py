from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)

from .models import CustomUser
from .serializers import UserSerializer, CreateUserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from utils.permissions import IsOwnerUserOrReadOnly
from campaign.models import Campaign


class UserList(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsOwnerUserOrReadOnly,)

# class UserCreate(CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CreateUserSerializer
#     permission_classes = (AllowAny,)