from django.contrib import admin
from .models import Teacher, Student, Group, Subject, Grade

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Grade)
