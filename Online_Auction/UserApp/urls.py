from django.urls import path
from .views import UserRegistration, AccountVerify,User_ActivationDetails,Bank_Details, AccountReactivate

urlpatterns = [
    path('create/', UserRegistration.as_view(), name='add'),
    path('verify/<token>/', AccountVerify.as_view(), name='activate'),
    path('user/<int:pk>/', User_ActivationDetails.as_view(),name="details"),
    path('user/<uid>/<token>/', AccountReactivate.as_view(),name="reactivate"),
    path('bankdetails/',Bank_Details.as_view(),name='bank')
]
