
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AuctionDetails, AllBids
from .serializers import AuctionDetailsSerializer, AllBidSerializer
from datetime import date

# Create your views here.


class Auction_Details(APIView):
    def post(self, request,format=None):
        try:
            serializer = AuctionDetailsSerializer(data=request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(data=serializer.data, status=201)
        except Exception as e:
            print(e)
            return Response(data={'detail': 'Error'}, status=400)
    
    def get(self,request,format=None):
        current_date = date.today()
        obj = AuctionDetails.objects.filter(auction_date=current_date)
        serializer = AuctionDetailsSerializer(obj,many=True)
        return Response(data=serializer.data, status=200)


class AuctionBids(APIView):
    def get(self, request, auction_id, format=None):
        try:
            auction = AuctionDetails.objects.get(auction_id=auction_id)
            auction_serializer = AuctionDetailsSerializer(auction)

            return Response(auction_serializer.data, status=status.HTTP_200_OK)
        
        except AuctionDetails.DoesNotExist:
            return Response({"detail": "Auction not found."}, status=status.HTTP_404_NOT_FOUND)


