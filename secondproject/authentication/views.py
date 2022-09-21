from contextlib import redirect_stderr
from email import message
from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request,"authentication/index.html")

def signup(request):

    if request.method == "POST":
        #username = request.POST.get('username')
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()

        messages.success(request,"Your account has been successfully created.")

        return redirect('signin')

    return render(request,"authentication/signup.html")

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request,user)
            firstname = user.first_name
            return render(request,"authentication/index.html", {'fname': firstname})
        else:
            messages.error(request,"Bad Credential!")
            return redirect('home')

    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"logout successfully")
    return redirect('home')
