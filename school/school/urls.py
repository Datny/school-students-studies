from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("teachers/", views.teachers, name="teachers"),
    path("students/", views.students, name="students"),
    path("grades/", views.grades, name="grades"),
    path("groups/", views.groups, name="groups"),
    path("subjects/", views.subjects, name="subjects"),
    path("login/", views.login, name="login"),
    re_path(r"^account/", include("account.urls")),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
