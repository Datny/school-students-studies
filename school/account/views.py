from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib import auth

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("authentication success")
                else:
                    return HttpResponse("Account is blocked")
            else:
                return HttpResponse("Bad username or password")
    else:
        form = LoginForm()
    return render(request, "account/login.html", {"form": form})


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST["username"])
                return render(request, 'account/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST["username"], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'account/signup.html', {'error': 'Passwords must match'})
    else:
        return render(request, 'account/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST["username"],password=request.POST["password"])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'account/login.html')


def logout(request):
     #if request.method == 'POST':
        auth.logout(request)
        return render(request, 'account/login.html')
