from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import CustomUser
from .serializers import UserSerializer 
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from utils.permissions import IsOwnerUserOrReadOnly


class UserList(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerUserOrReadOnly,)
