from django.db import models
from django.utils import timezone


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.name


####
class Group(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(Teacher)
    create_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name


####
class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


####
class Student(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name


####
def grades(value):
    if value < 1 or value > 6:
        raise ValidationError("Grade should be a from 1 to 6 number")


class Grade(models.Model):
    grade = models.IntegerField(validators=[grades], default=1)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now())
    descritption = models.CharField(max_length=100)

    def __str__(self):
        return self.grade
