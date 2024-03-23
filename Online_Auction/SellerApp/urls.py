from django.urls import path
from .views import ProductImageVerificationAPIView, ProductVerificationAPIView,ProductDetails

urlpatterns = [
    path('piv/', ProductImageVerificationAPIView.as_view, name ='product-image-verification'),
    path('pv/',  ProductVerificationAPIView.as_view(), name='product-verification'),
    path('detail/',ProductDetails.as_view(),)
]


