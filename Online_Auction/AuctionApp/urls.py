from django.urls import path
from .views import Auction_Details, AuctionViewSet

urlpatterns = [
    path('scedule/',  Auction_Details.as_view() , name =' schedule_auction'),
    path('thisweek/',  AuctionViewSet.as_view() , name =' thisweek_schedule_auction'),
]