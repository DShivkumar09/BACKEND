from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response



class ProductAPI(APIView):
    def post(self, request):
        try:
            serializer = ProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=201)
        except Exception as e:
            print(e)
            return Response(data=serializer.errors, status=400)
    def get(self, request):
        try:
            product = Product.objects.all()
            serializer = ProductSerializer(product, many=True)
            return Response(data=serializer.data, status=200)
        except:
            return Response(data={'details':'Data not found'}, status=400)

class ProductDetailsAPI(APIView):
    def get(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(data=serializer.data, status=200)
        except:
            return Response(data={'details':'Fetching error on details api'})