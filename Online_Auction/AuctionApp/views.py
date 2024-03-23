from rest_framework.views import APIView
from .serializers import BiddersSerializer, CurrentAcutionSerializer
from .models import Bidders, CurrentAuctions
from rest_framework.response import Response



class BiddersAPI(APIView):
    def post(self, request):
        try:
            serializer = BiddersSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=201)
        except Exception as e:
            print(e)
            return Response(data=serializer.errors, status=400)
        
    def get(self, request):
        try:
            bidder = Bidders.objects.all()
            serializer = BiddersSerializer(bidder, many=True)
            return Response(data=serializer.data, status=200)
        except:
            return Response(data={'details':'Data not found'}, status=400)
        
class CurrentAcutionAPI(APIView):
    def get(self, request):
        try:
            current = CurrentAuctions.objects.all()
            serializer = CurrentAcutionSerializer(current, many=True)
            return Response(data=serializer.data, status=200)
        except:
            return Response(data={'details':'Data not found'}, status=400)
            