from django.contrib import admin
from DWS.models import RecievedEmail


class RecievedEmailAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "date",
        "message",
    )


admin.site.register(RecievedEmail, RecievedEmailAdmin)
