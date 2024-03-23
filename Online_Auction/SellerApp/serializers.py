from rest_framework import serializers
from .models import Product, ProductImages


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    p_images = serializers.ListField(child=serializers.ImageField(), write_only=True)
    product_images = ProductImagesSerializer(read_only=True, many=True)
    
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        p_images = validated_data.pop('p_images')
        obj =  super().create(validated_data)

        for p_image in p_images:
            p = ProductImages(product=obj, product_image= p_image)
            p.save()
        return obj

