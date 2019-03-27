from django.conf.urls import url
from . import views
from django.urls import re_path


urlpatterns = [re_path(r"^login/$", views.user_login, name="login")]
