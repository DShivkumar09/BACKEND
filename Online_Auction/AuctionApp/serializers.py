from rest_framework import serializers
from .models import AuctionDetails, AllBids

class AllBidSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllBids
        fields = '__all__'


class AuctionDetailsSerializer(serializers.ModelSerializer):
    auctio_start_time = serializers.TimeField(format="%H:%M")
    auctio_end_time = serializers.TimeField(format="%H:%M")

    allauctionbids = AllBidSerializer(many=True, read_only=True)
    class Meta:
        model = AuctionDetails
        fields = '__all__'


