from DWS.api.serializers import EmailSerializer
from DWS.models import RecievedEmail
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status, exceptions


class RecievedEmailView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_message = serializer.save()
            if new_message:
                # send email
                return Response(status=status.HTTP_201_CREATED)
            # Log responce
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
