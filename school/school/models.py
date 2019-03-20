from django.db import models
from django.utils import timezone

class Teacher(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)

    
    def __str__(self):
        return self.title