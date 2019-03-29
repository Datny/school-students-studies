from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "group", "subjects")

class AddTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ("name", "description")

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ("grade", "student", "teacher", "subject", "date", "descritption")        
