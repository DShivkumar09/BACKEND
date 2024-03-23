from rest_framework import serializers
from SellerApp.serializers import ProductSerializer
from .models import Bidders, CurrentAuctions, AuctionDetails


class BiddersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bidders
        fields = '__all__'

class AuctionDetailsSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = AuctionDetails
        fields = "__all__"

class CurrentAcutionSerializer(serializers.ModelSerializer):
    auction = AuctionDetailsSerializer(read_only=True)

    class Meta:
        model = CurrentAuctions
        fields = '__all__'


