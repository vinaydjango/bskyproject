from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contactsapp.models import Contact
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'your now login')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentioals')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')
def logout(request):
    if request.method =='POST':
        auth.logout(request)


    return render(request,'accounts/login.html')
def register(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['pass']
        cpassword=request.POST['cpass']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That user is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That email is taken')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=fname,last_name=lname)
                    user.save()
                    messages.success(request,'you are register successfully')
                    return redirect('login')
        else:
            messages.error(request,'password do not matches')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')
def dashboard(request):
    user_contacts=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    return render(request,'accounts/dashboard.html',{'user_con':user_contacts})
