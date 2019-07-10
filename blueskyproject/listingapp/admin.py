from django.contrib import admin
from listingapp.models import Listing
class ListingAdmin(admin.ModelAdmin):
    list_display=['title']
admin.site.register(Listing,ListingAdmin)
