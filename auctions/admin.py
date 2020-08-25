from django.contrib import admin
from .models import User,listing,watchlist,bidding
# Register your models here.
admin.site.register(listing)
admin.site.register(watchlist)
admin.site.register(bidding)