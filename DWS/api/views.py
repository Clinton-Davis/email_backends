from DWS.api.serializers import EmailSerializer
from DWS.models import RecievedEmail
from rest_framework import exceptions, generics, serializers, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from DWS.email import DWSEmail
from django.conf import settings


class ReceivedEmailView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_message = serializer.save()
            if new_message:
                context = {"email": new_message}
                DWSEmail(self.request, context).send(settings.DEV)
                # send email
                return Response(status=status.HTTP_201_CREATED)
            # Log response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowEmailView(generics.ListAPIView):
    queryset = RecievedEmail.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [AllowAny]


class WakeUpView(APIView):
    permission_classes = [AllowAny]
    serializer_class = EmailSerializer

    def get(self, request):
        return Response({"message": "I'm awake"})
