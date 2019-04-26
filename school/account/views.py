import csv, io
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, InviteForm
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Invite, CsvFile
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.utils.crypto import get_random_string
from django.core.validators import validate_email



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
    if request.method == "POST" and 'send' in request.POST:
        form = InviteForm(request.POST)
        if form.is_valid():
            reg_token = get_random_string(length=12)
            form.reg_token = reg_token
            form.save()
            last_email = Invite.objects.last()
            msg = "Invitation has been sent to: " + str(last_email)
            subject = request.POST.get('subject', 'Registration link for school')
            message = request.POST.get('message', reg_token)
            from_email = request.POST.get('from_email', 'sqlacc@registration.com')
            print(last_email)

            if subject and message and from_email:
                try:
                    send_mail(subject, message, from_email, [last_email])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return render(request, 'account/invite.html', {'msg': msg, 'form': form})
            return render(request, 'account/invite.html', {'msg': msg, 'form': form})
    else:
        form = InviteForm()
    return render(request, 'account/invite.html', {'form': form})


def email_invitations(request):
    prompt = {"order": "Order of CSV file should be : name,surname, email adress", "form": InviteForm()}
    if request.method == "POST" and 'upload' in request.POST:

        csv_file = request.FILES['file']

        if not csv_file.name.endswith(".csv"):
            return render(request, 'account/invite.html', {"badfiletype": "Uploaded file is not CSV","form": InviteForm()})

        data_set = csv_file.read().decode("UTF-8")
        io_string = io.StringIO(data_set)
        next(io_string)
        invalid_emails_list = []
        for column in csv.reader(io_string, delimiter=",", quotechar="|"):
            try:
                validate_email(column[2].strip())
                _, created = CsvFile.objects.update_or_create(
                first_name=column[0],
                last_name=column[1],
                email=column[2],
            )
            except:
                invalid_emails_list.append(str(column[2]))
                print(invalid_emails_list)

        context = {"invalid_emails": invalid_emails_list, "form": InviteForm()}
        return render(request, 'account/invite.html', context)

    else:
        return render(request, 'account/invite.html', prompt)
