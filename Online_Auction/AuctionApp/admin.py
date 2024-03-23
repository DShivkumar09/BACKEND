from django.contrib import admin
from .models import AuctionDetails, AllBids, Bidders


# Register your models here.

@admin.register(AuctionDetails)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('product','auction_id','auction_date','auctio_start_time','auctio_end_time','increment_amount')


@admin.register(AllBids)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('bid_amount', 'auction', 'bidder')


@admin.register(Bidders)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('CHOICES', 'bidder_type', 'bidder')
