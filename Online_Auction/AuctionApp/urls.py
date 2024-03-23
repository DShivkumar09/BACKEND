from django.urls import path
from .views import BiddersAPI, CurrentAcutionAPI


urlpatterns = [
    path('bidder/', BiddersAPI.as_view()),
    path('current/', CurrentAcutionAPI.as_view())
]