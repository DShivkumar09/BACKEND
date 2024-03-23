from celery import shared_task
from .models import AuctionDetails
from .serializers import  AuctionDetailsSerializer
from time import sleep
from datetime import date
from rest_framework.response import Response
from celery import Celery
from .models import CurrentAuctions ,CurrentBids, AllBids, ClosingBids
from django.db.models import Max

@shared_task
def my_task():
    current_date = date.today()
    #CurrentAuctions.objects.all().delete()
    obj = AuctionDetails.objects.filter(auction_date = current_date)
    for data in obj:
        auction = data
        obj1, _ = CurrentAuctions.objects.get_or_create(auction = auction)
        
        sleep(1)
    return  "Task Completed"

@shared_task
def my_task2():
    obj = CurrentBids.objects.all()

    for data in obj:
        ad = data.auction.auction
        obj2, _ = AllBids.objects.get_or_create( auction=ad,bidder=data.bidder,bid_amount=data.bid_amount)
    current_auction = CurrentAuctions.objects.all()
    for obj1 in current_auction:
    # obj1 = current_auction[0]
        print(obj1)
        max_bid = obj1.auction_bids.aggregate(Max('bid_amount'))
        mbid = obj1.auction_bids.get(bid_amount=max_bid.get('bid_amount__max'))
        # closing_bid_amount = mbid
        # print(closing_bid_amount)
        bidder = mbid.bidder
        ad = obj1.auction
        all_bids = obj1.auction_bids.all()
        print(all_bids)
        obj2, _ = ClosingBids.objects.get_or_create(closing_bid_amount=mbid.bid_amount,bidder=bidder,auction=obj1.auction)
    
    # AllBids.objects.filter(auction = ad, bidder = data.bidder).update(bid_amount = maxbid)
    # ClosingBids.objects.get_or_create(auction = ad, bidder=data.bidder,closing_bid_amount = data.bid_amount)
    # maxbid = ClosingBids.objects.filter(auction_id=data.auction).order_by('-closing_bid_amount').first().closing_bid_amount
    sleep(1)
        
    return 'Task-2 Completed'

