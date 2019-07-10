from django.contrib import admin
from realtorapp.models import Realtor
class RealtorAdmin(admin.ModelAdmin):
    list_display=['name','email','phone']
admin.site.register(Realtor,RealtorAdmin)
