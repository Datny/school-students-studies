from django import forms
from .models import Invite


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ('email',)


class SendSmsForm(forms.Form):
    sms_text = forms.CharField(max_length=155,widget=forms.Textarea)
    reciver = forms.CharField(max_length=12)






