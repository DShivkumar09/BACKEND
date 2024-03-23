from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, ProductImages
from .serializers import ProductSerializer, ProductImagesSerializer
from rest_framework import status
import logging

# Create your views here.

logger = logging.getLogger('mylogger')

class ProductVerificationAPIView(APIView):
    def post(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        product.product_verify = True
        product.save()

        logger.info(f"Product {product_id} has been verified by {request.user}")
        return Response({'message': 'Product verified'}, status=status.HTTP_200_OK)
    
    

class ProductImageVerificationAPIView(APIView):
    def post(self, request, product_id):
        product = Product.objects.get(pk=product_id)

        image_data = request.data.get('product_image')
        serializer = ProductImagesSerializer(data={'product': product_id, 'product_image': image_data})
        if serializer.is_valid():
            serializer.save()

            logger.info(f"Image uploaded for product {product_id} by {request.user}")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetails(APIView):
    def get(self, request):
        try:
            product = Product.objects.all()
            serializer = ProductSerializer(product, many=True)
            logger.info('Data fetch successfully')
            return Response(data=serializer.data, status=200)
        except:
            logger.error('Data fetching error')
            return Response(data={'details':'there is an error fetching data'}, status=400)