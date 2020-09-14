from django.contrib import admin
from auctions.models import User, Category, Listing, Watchlist, Bid


class ListingsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing, ListingsAdmin)
admin.site.register(Watchlist)
admin.site.register(Bid)
