from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, \
    UserSerializer as BaseUser
from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password','email',\
             'first_name', 'last_name']

class UserSerializer(BaseUser):
    class Meta(BaseUser.Meta):
        fields = ['id','username', 'email', 'first_name', 'last_name']