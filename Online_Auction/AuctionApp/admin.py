from django.contrib import admin
from .models import AuctionDetails, CurrentAuctions, CurrentBids, Bidders, AllBids, ClosingBids


# Register your models here.

@admin.register(AuctionDetails)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product','auction_id','auction_date','auctio_start_time','auctio_end_time','increment_amount')

@admin.register(CurrentAuctions)
class CurrentAuctionAdmin(admin.ModelAdmin):
    list_display = ['current_auction_id', 'auction']

@admin.register(CurrentBids)
class CurrentBidsAdmin(admin.ModelAdmin):
    list_display = ['bid_amount', 'auction', 'bidder']
    
@admin.register(Bidders)
class BiddersAdmin(admin.ModelAdmin):
    list_display = ['CHOICES', 'bidder_type', 'bidder']
    
@admin.register(AllBids)
class AllBidsAdmin(admin.ModelAdmin):
    search_fields = ['bid_amount','auction','bidder']
    
@admin.register(ClosingBids)
class ClosingBidsadmin(admin.ModelAdmin):
    list_display = ['closing_bid_amount','bidder','auction'] 