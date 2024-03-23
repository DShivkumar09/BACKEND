from django.contrib import admin


from django.contrib import admin
from .models import AuctionDetails, CurrentAuctions


# Register your models here.

@admin.register(AuctionDetails)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product','auction_id','auction_date','auctio_start_time','auctio_end_time','increment_amount')

@admin.register(CurrentAuctions)
class AcutionAdmin(admin.ModelAdmin):
    list_display = ('current_auction_id', 'auction')