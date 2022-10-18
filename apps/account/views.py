from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .serializers import UserRegistrationSerializer


User = get_user_model()


class RegistrationView(APIView):
    @swagger_auto_schema(request_body=UserRegistrationSerializer)
    def post(self, request: Request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Thank for registration! Please activate your account',
                status=status.HTTP_201_CREATED
            )

# TODO: Активация, Смена пароля, Удаление аккаунта, Восстановление пароля
# TODO: Подключить celery, redis
# TODO: Исправить HTML