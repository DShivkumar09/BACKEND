from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response


class ShowProductListAPI(APIView):
    def get(self, request):
        obj = Product.objects.all()
        serializer = ProductSerializer(obj, many=True)    
        return Response(data=serializer.data, status=200)
    

class VerifiedProductListView(APIView):
    def get(self, request):
        verified_products = Product.objects.filter(product_verify=True)
        serializer = ProductSerializer(verified_products, many=True)
        return Response(serializer.data,status=200)
       