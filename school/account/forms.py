from django import forms
from .models import Invite


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ('email',)
