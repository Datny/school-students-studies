from django.shortcuts import render, redirect
from .models import Teacher
from .models import Student
from .forms import AddTeacherForm


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
    return render(request, "teachers.html", {"form": form, "teachers": teachers})


def students(request):
    students = Student.objects.order_by("name")
    return render(request, "students.html", {"students": students})
