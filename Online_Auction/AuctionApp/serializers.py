from rest_framework import serializers
from .models import AuctionDetails


class AuctionDetailsSerializer(serializers.ModelSerializer):
    auctio_start_time = serializers.TimeField(format="%H:%M")
    auctio_end_time = serializers.TimeField(format="%H:%M")
    class Meta:
        model = AuctionDetails
        fields = '__all__'
        
class AuctionSerializer(serializers.ModelSerializer):
     auctio_start_time = serializers.TimeField(format="%H:%M")
     auctio_end_time = serializers.TimeField(format="%H:%M")
     class Meta:
        model = AuctionDetails
        fields = '__all__'