from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        user=request.POST['username']
        first = request.POST['first_name']
        last = request.POST['last_name']
        mail = request.POST['email']
        i_password = request.POST['password']
        c_password = request.POST['password1']

        if i_password == c_password:
            if User.objects.filter(username=user).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,"mail id exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=user,password=i_password,first_name=first,last_name=last,email=mail)
                user.save()
                return redirect('login')

        else:
            messages.info(request,"password doesnt match")
            return redirect('register')
        # return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
