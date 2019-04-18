from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings

from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),

    path("teachers/", views.teachers, name="teachers"),
    path("<int:pk>/teacher_edit/", views.teacher_edit, name="teacher_edit"),

    path("students/", views.students, name="students"),

    path("<int:pk>/student_edit/", views.student_edit, name="student_edit"),

    path("grades/", views.grades, name="grades"),
    path("<int:pk>/grade_edit/", views.grade_edit, name="grade_edit"),

    path("groups/", views.groups, name="groups"),
    path("<int:pk>/group_edit/", views.group_edit, name="group_edit"),

    path("subjects/", views.subjects, name="subjects"),
    path("<int:pk>/subject_edit/", views.subject_edit, name="subject_edit"),
    
    path("<int:pk>/group/", views.show_group, name="show_group"),

    path("account/", include("account.urls")),
    re_path(r"^account/", include("account.urls")),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      re_path(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

