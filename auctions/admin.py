from django.contrib import admin
from auctions.models import User, Category, Listing


class ListingsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing, ListingsAdmin)
