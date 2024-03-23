from typing import Any, Dict
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data =  super().validate(attrs)
        data['role'] = self.user.role
        print(data)
        return data

