from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Country(models.Model):
    country_id = models.BigAutoField(primary_key=True)
    country_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=5)


class State(models.Model):
    state_id = models.BigAutoField(primary_key=True)
    state_name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class City(models.Model):
    city_id = models.BigAutoField(primary_key=True)
    city_name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE)


class User(AbstractUser):
    CHOICES = [('user', 'user'), ('admin', 'admin')]
    role = models.CharField(max_length=5, choices=CHOICES, default='admin')
    aadhar_card = models.ImageField(blank=True, upload_to='aadhar/') 
    pan_card = models.ImageField(blank=True, upload_to='pan_card/')
    passport_front = models.ImageField(blank=True, upload_to='passport_front/')
    passport_back = models.ImageField(blank=True, upload_to='passport_back/')
    contact_no = PhoneNumberField(blank=True, region='IN')
    address = models.TextField(blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, related_name='users')
    pincode = models.PositiveIntegerField(null=True, blank=True)
    

class BankInformation(models.Model):
    bank_name = models.CharField(max_length=100)
    bank_ifsc_code = models.CharField(max_length=20)
    bank_address = models.TextField()
    bank_account_number = models.CharField(max_length=20, unique=True)
    branch_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bank_details')
    
    
    