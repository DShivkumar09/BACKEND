from rest_framework.views import APIView
from .models import User
# from .models import State
# from .models import  City
from .serializers import UserSerializer, CountrySerializer, StateSerializer,CitySerializer
import logging
from django.utils.encoding import force_bytes,force_str
from rest_framework.response import Response
from django.conf import  settings
from .utils import EmailThread
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .token import account_activation_token
from django.urls import reverse
import jwt
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUserOrCreateOnly, IsAccountOwner
from rest_framework.decorators import permission_classes,authentication_classes
from .serializers import BankSerializer
from .models import BankInformation

logger = logging.getLogger('mylogger')


class UserRegistration(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAdminUserOrCreateOnly]
    def post(self, request, format=None):
            try:
                serializer = UserSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                obj = serializer.save()
                obj.is_active = False
                obj.save()
                domain = get_current_site(request=request).domain
                token = account_activation_token.make_token(obj)
                uid = urlsafe_base64_encode(force_bytes(obj.pk))
                relative_url = reverse('reactivate',kwargs={'token':token,'uid':uid})
                absolute_url = f'http://%s'%(domain+relative_url,)
                message = "Hello %s,\n\tThank you for creating account with us. please click on the link below"\
                    "to activate your account\n %s"%(obj.username,absolute_url,)
                subject = "Account Activation Email"
                EmailThread(subject=subject, message=message, recipient_list=[obj.email], from_email=settings.EMAIL_HOST_USER).start()
                return Response({"Message":"Please check your email to activate your account"},status=201)
            except Exception as e :
                print(e)
                logger.error("Error in Creating the Student")
                return Response(data={'detail': 'Link in expired'}, status=404)

    def get(self,request,format=None):
        try:
            obj = User.objects.all()
            serializer = UserSerializer(obj, many=True)
            logger.info('User List Retrieved Successfully')
            return Response(data=serializer.data,status=200)
        except Exception as e:
            logger.error('Error In Featching  Users Data')
            return Response(data={"message":str(e)},status=404)
        

class AccountVerify(APIView):

    def get(self, request, token=None):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY,algorithms=['HS256'])
            user = User.objects.get(pk=payload.get('user_id'))
            user.is_active = True
            user.save()
            return Response(data={'detail': 'Account activated successfully'}, status=200)
        except jwt.DecodeError:
            return Response(data={'detail': 'Token in expired'}, status=400)
        except jwt.ExpiredSignatureError:
            return Response(data={'detail': 'Link in expired'}, status=400)
        
      
class User_ActivationDetails(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    def delete(self,request,pk):
        try:
            user = User.objects.get(pk=pk)
            user.is_active = False
            user.save()
            domain = get_current_site(request=request).domain
            token = account_activation_token.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            relative_url = reverse('reactivate',kwargs={'uid': uid, 'token':token})
            absolute_url = f'http://%s'%(domain+relative_url,)
            message = "Hello %s,\n\tThank you for creating account with us. please click on the link below"\
                "to activate your account\n %s"%(user.username,absolute_url,)
            subject = "Account Activation Email"
            EmailThread(subject=subject, message=message, recipient_list=[user.email], from_email=settings.EMAIL_HOST_USER).start()
            return Response({"Message":"Please check your email to activate your account"},status=201)
        except Exception as e :
            print(e)
            logger.error("Error in Creating the User")
            return Response(data={'detail': 'Link in expired'}, status=404)
        
       
# class User_Activation(APIView):
#     def post(self,request,pk):
#         try:
#             serializer = UserSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             obj = serializer.save()
#             obj.is_active = False
#             obj.save()
            
class AccountReactivate(APIView):        
    def get(self, request, uid, token):
        
            try:
                user_id = force_str(urlsafe_base64_decode(uid))
                print(user_id)
                user = User.objects.get(pk= user_id)
            except(TypeError,ValueError,OverflowError,User.DoesNotExist)as e:
                return Response(data={'details':'there is an Error'},status=400)
            if account_activation_token.check_token(user=user, token=token):
                user.is_active = True
                user.save()
                return Response(data={'details':'Account Activated SuccesFully'},status=200)
            return Response(data={'details':'Account link Invalid'},status=400)
        
class Bank_Details(APIView):
    def post(self,request):
        try:
            serializer = BankSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info("Bank Details Added Successfully")
            return Response(data=serializer.data,status=201)
        except  Exception as e:
            print(e)
            logger.error("Error in Adding Bank Details ")
            return Response(data={'details':'Error in Bank Details'},status=400)
        
    def get(self,request):
        try:
            obj = BankInformation.objects.all()
            serializer = BankSerializer(obj,many=True)
            logger.info("Data FetchSuccessFully")
            return Response(data=serializer.data,status=200)
        except  Exception as e:
            logger.error("Error in data Featching")
            return Response(data=None,status=404)    
    