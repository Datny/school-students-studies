from django.shortcuts import render, redirect
from .models import Teacher
from .models import Student
from .forms import StudentForm
from django import forms
from .forms import AddTeacherForm
from .models import Grade
from .forms import GradeForm
from .forms import LoginForm


def login(request):
    form = LoginForm
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, "home.html")


def teachers(request):
    teachers = Teacher.objects.order_by("name")

    if request.method == "POST":
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("teachers")
    else:
        form = AddTeacherForm()
    return render(request, "teachers.html", {"form": form, "teachers": teachers},)


def students(request):
    students = Student.objects.order_by("name")
    

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students")
    else:
        form = StudentForm()
    return render(request, "students.html", {"form": form, "students": students})

def grades(request):
    grades = Grade.objects.order_by("grade")
    

    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("grades")
    else:
        form = GradeForm()
    return render(request, "grades.html", {"form": form, "grades": grades})
