
from rest_framework import serializers
from .models import CustomUser

from campaign.models import Campaign

from django.core.serializers import serialize


# class UserListSerializer(serializers.ListSerializer):

#     @property
#     def data(self):
#         # call the super() to get the default serialized data
#         serialized_data =  super(UserListSerializer, self).data       
#         custom_representation = {'data': serialized_data} # insert the above response in a dictionary
#         return custom_representation


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone', 'image')
        # list_serializer_class = UserListSerializer