from rest_framework import serializers
from rest_framework.permissions import (AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,)

from ..models import *

class UserBookCreateSerializer(serializers.ModelSerializer):

    def perform_create(self, serializer):
        #To associate current user wih the new model bieng created
        serializer.save(user = self.request.user.profile)

    class Meta:
        model = UserBook
        fields =['isbn','status']

class UserBookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBook
        fields =['isbn','status','user']


class UserBookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBook
        fields =['status']

class UserBookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBook
        fields =['isbn','status','user']
