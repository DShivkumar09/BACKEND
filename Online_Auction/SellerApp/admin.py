from django.contrib import admin
from .models import Product, ProductImages


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id','product_name', 'product_description', 'product_manufacture_year', 'product_base_price', 'owner', 'product_verify')

@admin.register(ProductImages)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product','product_image')