from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.views.generic.edit import UpdateView
from .models import Teacher, Student, Grade, Group, Subject
from .forms import TeacherForm, StudentForm, GradeForm, GroupForm, SubjectForm
from django.contrib.auth.decorators import login_required




@login_required(login_url=("/account/login"))
def home(request):
    return render(request, "home.html")


@login_required(login_url=("/account/login"))
def teachers(request):
    teachers = Teacher.objects.order_by("name")

    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("teachers")
    else:
        form = TeacherForm()
    return render(request, "teachers.html", {"form": form, "teachers": teachers})

def teacher_edit(request,pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teachers = Teacher.objects.order_by("name")

    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect("teachers")
    else:
        form = TeacherForm(instance=teacher)
    return render(request, "teachers.html", {"form": form, "teachers": teachers})

@login_required(login_url=("/account/login"))
def students(request):
    students = Student.objects.order_by("group", "name")
    
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students")
    else:
        form = StudentForm()
    return render(request, "students.html", {"form": form, "students": students})

def student_edit(request,pk):
    student = get_object_or_404(Student, pk=pk)
    students = Student.objects.order_by("group", "name")

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("students")
    else:
        form = StudentForm(instance=student)
    return render(request, "students.html", {"form": form, "students": students})


@login_required(login_url=("/account/login"))
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


def grade_edit(request,pk):
    grade = get_object_or_404(Grade, pk=pk)
    grades = Grade.objects.order_by("grade")

    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect("grades")
    else:
        form = GradeForm(instance=grade)
    return render(request, "grades.html", {"form": form, "grades": grades})

@login_required(login_url=("/account/login"))
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

def group_edit(request,pk):
    group = get_object_or_404(Group, pk=pk)
    groups = Group.objects.order_by("name")

    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect("groups")
    else:
        form = GroupForm(instance=group)
    return render(request, "groups.html", {"form": form, "groups": groups})

@login_required(login_url=("/account/login"))
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
def subject_edit(request,pk):
    subject = get_object_or_404(Subject, pk=pk)
    subjects = Subject.objects.order_by("name")

    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect ("subjects")
    else:
        form = SubjectForm(instance=subject)
    return render(request, "subjects.html", {"form": form, "subjects": subjects})

def students_grades(request,pk):
    student = get_object_or_404(Student, pk=pk)
    subjects = student.subjects.all()
    grades = Grade.objects.filter(student__id=pk)

    grades_dict = {}
    for subject in subjects:
        subject_grades = grades.filter(subject=subject.id)
        grades_list = [grade.grade for grade in list(subject_grades)]
        mean = sum(grades_list)/len(grades_list) if len(grades_list) > 0 else ""

        grades_dict[subject.name] = [
            ", ".join([str(grade.grade) for grade in list(subject_grades)]),
            mean
        ]

    return render(
        request, "student.html",
        {"student": student, "grades_dict": grades_dict}
    )
