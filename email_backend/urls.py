from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("email_backends_admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("DWS/", include("DWS.api.urls", namespace="DWS")),
]
