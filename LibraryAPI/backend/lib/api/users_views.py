from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.lib.serializers.users_serializers import UserSerializer
from backend.lib.services.users_services import register_user, login_user
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        user, errors = register_user(serializer)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        tokens, errors = login_user(username, password)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(username=username)
        return Response({
            "id": user.id,
            "username": user.username,
            **tokens
        }, status=status.HTTP_200_OK)
