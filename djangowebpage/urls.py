from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from personal.views import (
    home_screen_view,
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("main.urls", namespace="main")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()