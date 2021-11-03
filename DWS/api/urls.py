from django.urls import path
from DWS.api.views import RecievedEmailView, ShowEmailView, WakeUpView


app_name = "DWS"

urlpatterns = [
    path("v1/post_email/", RecievedEmailView.as_view(), name="post_email"),
    path("v1/get_emails/", ShowEmailView.as_view(), name="get_email"),
    path("v1/wake_up/", WakeUpView.as_view(), name="wake_up"),
]
