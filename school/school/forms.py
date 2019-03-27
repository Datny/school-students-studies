from django import forms
from .models import Student
from .models import Teacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name",)
from .models import Teacher


class AddTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ("name",)
