from django.shortcuts import render, get_list_or_404
from listingapp.models import Listing
from realtorapp.models import Realtor
from django.core.paginator import Paginator
def home_view(request):
    list=Listing.objects.all().order_by('-id')
    return render(request,'home.html',{'list':list})

def about_view(request):
    list=Realtor.objects.all().order_by('-id')[0:4]
    return render(request,'about.html',{'list':list})

def properties_view(request):
    list=Listing.objects.all().order_by('-id')
    paginator = Paginator(list,6)
    page = request.GET.get('page')
    page_list = paginator.get_page(page)
    count= Listing.objects.all().count()
    return render(request,'properties.html',{'list':page_list,'count':count})

def property_view(request,id):
    list=Listing.objects.get(id=id)
    return render(request,'property.html',{'list':list})
