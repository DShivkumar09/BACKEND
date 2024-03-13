from django.db import models
from UserApp.models import User
from AuctionApp.models import AuctionDetails

# Create your models here.
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    auctions = models.ForeignKey(AuctionDetails, on_delete=models.CASCADE, related_name='auction_wishlist')