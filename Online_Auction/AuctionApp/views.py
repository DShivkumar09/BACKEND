from django.shortcuts import render
from SellerApp.views import Product
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AuctionDetails
from .serializers import AuctionDetailsSerializer, AuctionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets


class Auction_Details(APIView):
    def post(self, request, format=None):
        try:
            serializer = AuctionDetailsSerializer(data=request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(data=serializer.data,status=201)
        except Exception as e:
            print(e)
            return Response(data={'detail': 'Error'}, status=400)
    
    def get(self,request,format=None):
        obj = AuctionDetails.objects.all()
        serializer = AuctionDetailsSerializer(obj,many=True)
        return Response(data=serializer.data,status=200)
    
class AuctionViewSet(APIView):
    def get(self, request, format=None):
        auctions = AuctionDetails.get_auctions_for_this_week()
        serializer = AuctionSerializer(auctions, many=True)
        return Response(serializer.data)