from rest_framework import serializers
from .user import User

class UserSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField()

    # class Meta:
    #     model = User
    #     fields = ('name', 'password')
