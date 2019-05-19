from .models import Invite
from django import forms
from django.core import validators
import re



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ('email',)




def check_if_phone_number(value):
    pattern ="^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\.\/0-9]*$"
    match = re.search(pattern, value)

    if match == None:
        raise forms.ValidationError("This is not valid phone number")


class SendSmsForm(forms.Form):
    sms_text = forms.CharField(max_length=155,widget=forms.Textarea)
    reciver = forms.CharField(max_length=12, validators=[check_if_phone_number])






