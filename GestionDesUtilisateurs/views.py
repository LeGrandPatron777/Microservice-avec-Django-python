from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema


class CreateUserView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Créer un nouvel utilisateur",
        request_body=UserSerializer,
        responses={201: UserSerializer},
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserView(APIView):
    permission_classes = [AllowAny]  # Modification pour restreindre l'accès

    @swagger_auto_schema(
        operation_description="Mettre à jour un utilisateur",
        request_body=UserSerializer,
        responses={200: UserSerializer},
    )
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(
                {"error": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
