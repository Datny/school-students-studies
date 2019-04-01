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

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("name", "teachers", "create_date")        

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ("name", "teacher", "group")        
