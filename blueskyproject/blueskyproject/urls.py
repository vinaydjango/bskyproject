from django.contrib import admin
from django.urls import path, include
from pagesapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('about/', views.about_view),
    path('properties/', views.properties_view),

    path('property/<int:id>', views.property_view),
    path('accounts/',include('accountsapp.urls')),
    path('contacts/',include('contactsapp.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
