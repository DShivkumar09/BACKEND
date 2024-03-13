from django.db import models
from UserApp.models import User

# Create your models here.

class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    product_description = models.TextField()
    product_manufacture_year = models.PositiveIntegerField(blank=True)
    product_base_price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name='products')
    product_verify = models.BooleanField(default=False)

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    product_image = models.ImageField(upload_to='product_images/', blank=True)