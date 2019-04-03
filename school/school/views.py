from django.shortcuts import render, redirect
from .models import Teacher
from .models import Student
from .forms import StudentForm
from django import forms
from .forms import AddTeacherForm
from .models import Grade
from .forms import GradeForm
from .models import Group
from .forms import GroupForm
from .models import Subject
from .forms import SubjectForm

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

def groups(request):
    groups = Group.objects.order_by("name")
    

    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("groups")
    else:
        form = GroupForm()
    return render(request, "groups.html", {"form": form, "groups": groups})

def subjects(request):
    subjects = Subject.objects.order_by("name")
    

    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("subjects")
    else:
        form = SubjectForm()
    return render(request, "subjects.html", {"form": form, "subjects": subjects})
