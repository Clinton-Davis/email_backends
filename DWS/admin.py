from django.contrib import admin
from DWS.models import RecievedEmail


class RecievedEmailAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "type", "date", "time_frame", "goals", "date")


admin.site.register(RecievedEmail, RecievedEmailAdmin)
