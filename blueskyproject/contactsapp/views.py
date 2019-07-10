from django.shortcuts import render,redirect
from django.contrib import messages
from contactsapp.models import Contact
from django.core.mail import send_mail
def contact(request):
    if request.method == 'POST':
        listing_id=request.POST['list_id']
        listing=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realter_email=request.POST['realter_email']
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contained=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contained:
                messages.error(request,'you have already made an enquiry for this listing')
                return redirect('/property/'+listing_id)

        contact=Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()
        # send_mail(
        #   'property listing Enquiry',
        #   'there has been an enquiry for'+listing+'sign into the admin panel for me',
        #   'pythonvinay1234@gmail.com'
        #   [realter_email,pythonvinay1234@gmail.com],
        #   #fail_silently=False
        #
        # )
        subject=listing
        message=message
        from_email=email
        send_mail(subject,message,from_email , ['vinaykanthpamarthi@gmail.com'])
        messages.success(request,'your request has been submited, a realter will get back to you soon')
        return redirect('/property/'+listing_id)
