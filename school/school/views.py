from django.shortcuts import render
from .models import Teacher


def home(request):
    return render(request, "home.html")

def teachers(request):
    teachers = Teacher.objects.order_by("name")
    return render(request, "teachers.html", {"teachers": teachers})