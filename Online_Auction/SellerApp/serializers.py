from rest_framework import serializers
from .models import Product, ProductImages

class ProductSerializer:
    class Meta:
        model = Product
        fields = '__all__'


class ProductImagesSerializer:
    class Meta:
        model = ProductImages
        fields = '__all__'