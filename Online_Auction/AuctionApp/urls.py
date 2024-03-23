from django.urls import path
from .views import Auction_Details, AuctionBids

urlpatterns = [
    path('scedule/',  Auction_Details.as_view() , name =' schedule_auction'),
    path('bids/<auction_id>/', AuctionBids.as_view(), name= 'all_bids')
]