from django.contrib import admin
from .models import User,listing,watchlist,bidding
# Register your models here.
class watchlistAdmin(admin.ModelAdmin):
    filter_horizontal = ("items",)

admin.site.register(listing)
admin.site.register(watchlist,watchlistAdmin)
admin.site.register(bidding)
admin.site.register(User)