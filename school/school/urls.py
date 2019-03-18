from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [path("admin/", admin.site.urls),
               path("", views.home),
               
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
