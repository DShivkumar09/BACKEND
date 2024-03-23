from django.db import models
from UserApp.models import User
from SellerApp.models import Product

# Create your models here.

class AuctionDetails(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='auction')
    auction_id = models.BigAutoField(primary_key=True)
    auction_date = models.DateField(blank=True)
    auctio_start_time = models.TimeField(blank=True)
    auctio_end_time = models.TimeField(blank=True)
    increment_amount = models.FloatField(blank=True)

    def __str__(self) -> str:
        return f'{self.auction_id}'
    
class CurrentAuctions(models.Model):
    current_auction_id = models.BigAutoField(primary_key=True)
    auction = models.OneToOneField(AuctionDetails, on_delete=models.CASCADE, related_name='current_auction')
        
        
class Bidders(models.Model):
    CHOICES = [('automatic', 'automatic'),('manual', 'manual')]
    bidder_type = models.CharField(max_length=10, choices=CHOICES)
    bidder = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bidders')

class AutomaticBidding(models.Model):
    max_bid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    inc_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    bidder = models.ForeignKey(Bidders, on_delete=models.CASCADE, related_name='autobids')
    auction = models.ForeignKey(AuctionDetails, on_delete=models.CASCADE, related_name='auction_autobids')


class CurrentBids(models.Model):
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    auction = models.ForeignKey(CurrentAuctions, on_delete=models.CASCADE, related_name='auction_bids')
    bidder = models.ForeignKey(Bidders, on_delete=models.CASCADE, related_name='current_bids')

class AllBids(models.Model):
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    auction = models.ForeignKey(AuctionDetails, on_delete=models.CASCADE, related_name='allauctionbids')
    bidder = models.ForeignKey(Bidders, on_delete=models.CASCADE, related_name= 'allbids')

class ClosingBids(models.Model):
    closing_bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bidder = models.ForeignKey(Bidders, on_delete=models.CASCADE, related_name='closing_bids')
    auction = models.ForeignKey(AuctionDetails, on_delete=models.CASCADE, related_name='closing_auctions')


class Transactions(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction')
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_status = models.BooleanField(default=False)

