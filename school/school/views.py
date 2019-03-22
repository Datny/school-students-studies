from django.shortcuts import render
from .models import Teacher
from .models import Student


def home(request):
    return render(request, "home.html")

def teachers(request):
    teachers = Teacher.objects.order_by("name")
    return render(request, "teachers.html", {"teachers": teachers})

def students(request):
    students = Student.objects.order_by("name")
    return render(request, "students.html", {"students": students})