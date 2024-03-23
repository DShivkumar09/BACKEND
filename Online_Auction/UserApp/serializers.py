from rest_framework import serializers
from .models import User
from .models import Country
from .models import State
from .models import BankInformation
from django.core import  validators
from .models import City

class CountrySerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Country
        fields=('country')
        
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('state')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('city')

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    password = serializers.CharField(write_only=True, validators= [validators.MinLengthValidator(8), validators.MaxLengthValidator(20),validators.RegexValidator('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[#$.*_!@])[a-zA-Z0-9#$.*_!@]{8,20}$')])
    username = serializers.CharField(validators=[validators.RegexValidator(r'^[a-zA-Z0-9]*$')])
    class Meta:
        model = User
        fields = ('id','username','password','email','first_name','last_name','aadhar_card','pan_card','contact_no','address','pincode')
        
    def create(self, validated_data):
        obj = User.objects.create_user(**validated_data)
        obj.is_active = False
        obj.save()
        return obj
    
class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankInformation
        fields = '__all__'
        