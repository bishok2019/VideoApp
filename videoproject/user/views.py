from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser

def signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return render(request, "index.html")
        else:
            messages.error(request, "Invalid email or password!")
            return redirect(signin)
    return render(request, "signin.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        myuser = CustomUser.objects.create_user(username=username, email=email, password=password)
        myuser.email = email
        myuser.save()
        messages.success(request, "Registration successful!")
        return redirect(signin)
    return render(request, "signup.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return render(request, 'signin.html')
