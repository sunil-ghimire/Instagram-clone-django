from rest_framework.response import Response
from rest_framework import serializers
from users.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'full_name', 'address', 'profile_picture', 'following', 'followers')