from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, InviteForm
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Invite
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.utils.crypto import get_random_string



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
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'account/signup.html', {'error': 'Passwords must match'})
    else:
        return render(request, 'account/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'account/login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'account/login.html')




def invite(request):
    if request.method == "POST":
        form = InviteForm(request.POST)
        if form.is_valid():
            reg_token = get_random_string(length=12)
            last_email = Invite.objects.latest('email')
            msg = "Invitation has been sent to: " + str(last_email)
            subject = request.POST.get('subject', 'Registration link for school')
            message = request.POST.get('message', reg_token)
            from_email = request.POST.get('from_email', 'sqlacc@registration.com')
            form.save()
            if subject and message and from_email:
                try:
                    send_mail(subject, message, from_email, [last_email])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return render(request, 'account/invite.html', {'msg': msg})
            return render(request, 'account/invite.html', {'msg': msg})
    else:
        form = InviteForm()
    return render(request, 'account/invite.html', {'form': form})


