from django.db import models
from UserApp.models import User
from AuctionApp.models import AuctionDetails, Bidders

# Create your models here.

class SuccessAuctions(models.Model):
    auction = models.ForeignKey(AuctionDetails, on_delete=models.CASCADE, related_name='auctions')
    bidder = models.ForeignKey(Bidders, on_delete=models.CASCADE, related_name='s_bidder')
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='s_owner')

class CancelledAuctions(models.Model):
    CANCEL_CHOICES = [('owner', 'owner'), ('admin', 'admin')]
    auction = models.ForeignKey(AuctionDetails, on_delete=models.CASCADE, related_name='c_auction')
    cancellation_reason = models.TextField()
    cancelled_by = models.CharField(max_length=10, choices=CANCEL_CHOICES)