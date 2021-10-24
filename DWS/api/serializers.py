from rest_framework import fields, serializers
from DWS.models import RecievedEmail


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecievedEmail
        fields = "__all__"
