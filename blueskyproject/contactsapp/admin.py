from django.contrib import admin
from contactsapp.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','phone']
    list_display_links=['name']
    search_fields=['name','email','listing']
    list_per_page=25
admin.site.register(Contact,ContactAdmin)
