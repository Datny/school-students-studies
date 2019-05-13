from django.conf.urls import url
from . import views
from django.urls import re_path, path, include



#ALL PATHS BELLOW ARE ACCESIBLE ONLY AFTER /account/
urlpatterns = [
    re_path(r"^login/$", views.user_login, name="login"),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('invite', views.invite, name='invite'),
    path('invites', views.email_invitations, name='csvupload'),
    path('invites', views.send_mass_email, name='sendmass'),
]
