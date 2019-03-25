from django import forms
from .models import Teacher


class AddTeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ('name',)

