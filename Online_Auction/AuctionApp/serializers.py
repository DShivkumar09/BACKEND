from rest_framework import serializers
from .models import AuctionDetails

class AuctionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionDetails
        fields = '__all__'