from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


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
