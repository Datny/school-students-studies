from django.contrib import admin
<<<<<<< HEAD
from django.conf import settings
from django.urls import include, path

urlpatterns = [path("admin/", admin.site.urls)]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

=======
from django.urls import include, path
from . import views

urlpatterns = [path("admin/", admin.site.urls),
               path("", views.home),
               
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

>>>>>>> 076a63693524f5a29baf8d056918270c9b0d3ae4
    ] + urlpatterns
