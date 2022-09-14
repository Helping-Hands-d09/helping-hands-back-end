
from rest_framework import serializers
from .models import CustomUser

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
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'location', 'phone', 'image')
        # fields = "__all__"
        # list_serializer_class = UserListSerializer

# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ("username", 'email', 'password', 'first_name', 'last_name', 'phone', 'location',)
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         user = CustomUser(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user