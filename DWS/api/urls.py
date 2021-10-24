from django.urls import path
from DWS.api.views import RecievedEmailView


app_name = "DWS"

urlpatterns = [
    path("v1/email/", RecievedEmailView.as_view(), name="email"),
]
