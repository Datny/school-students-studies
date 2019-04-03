from django.contrib import admin
from django.urls import include, path,re_path
from django.conf import settings

from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("teachers/", views.teachers, name="teachers"),
    path("students/", views.students, name="students"),
    path("grades/", views.grades, name="grades"),
    path("<int:pk>/grade_edit/", views.grade_edit, name="grade_edit"),
    
    path("groups/", views.groups, name="groups"),
    path("subjects/", views.subjects, name="subjects"),
    
    re_path(r"^account/", include("account.urls")),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

