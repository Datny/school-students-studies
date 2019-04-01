from django.conf.urls import url
from . import views
from django.urls import re_path, path, include


urlpatterns = [
    re_path(r"^login/$", views.user_login, name="login"),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')

]
