from django.urls import path
from .views import ProductAPI, ProductDetailsAPI


urlpatterns = [
    path('product/', ProductAPI.as_view()),
    path('product/<int:pk>/', ProductDetailsAPI.as_view())
]