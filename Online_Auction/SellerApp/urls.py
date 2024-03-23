from django.urls import path
from .views import ShowProductListAPI,VerifiedProductListView

urlpatterns=[

    path('show/',ShowProductListAPI.as_view()),
     path('verified/', VerifiedProductListView.as_view(), name='verified-products'),
]
