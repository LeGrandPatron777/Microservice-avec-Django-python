from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Chambre, ReservationChambre
from .serializers import ChambreSerializer, ReservationChambreSerializer
import requests

from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import requests


class RechercheChambresAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Recherche de chambres d'hôtel",
        manual_parameters=[
            openapi.Parameter(
                "location",
                openapi.IN_QUERY,
                description="Emplacement de l'hôtel",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "checkIn",
                openapi.IN_QUERY,
                description="Date d'arrivée",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "checkOut",
                openapi.IN_QUERY,
                description="Date de départ",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "currency",
                openapi.IN_QUERY,
                description="Devise (par exemple CAD)",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "limit",
                openapi.IN_QUERY,
                description="Nombre limite de résultats",
                type=openapi.TYPE_INTEGER,
                default=100,
            ),
        ],
    )
    def get(self, request):
        # Récupérer les paramètres de la requête
        location = request.query_params.get("location")
        checkInDate = request.query_params.get("checkIn")
        checkOutDate = request.query_params.get("checkOut")
        currency = request.query_params.get(
            "currency", "CAD"
        )  # 'CAD' est une valeur par défaut
        limit = request.query_params.get("limit", 10)  # 100 est une valeur par défaut

        # Vérifier que les paramètres nécessaires sont présents
        if not location or not checkInDate or not checkOutDate:
            return Response({"error": "Paramètres manquants"}, status=400)

        # Construire l'URL avec les paramètres
        url = f"http://engine.hotellook.com/api/v2/cache.json?location={location}&checkIn={checkInDate}&checkOut={checkOutDate}&currency={currency}&token=6ccf4da559f0777e5a5c543cd67ca555&limit={limit}"

        # Effectuer la requête à l'API externe
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())
        else:
            return Response(response.text, status=response.status_code)


class ReservationChambreAPIView(APIView):
    def post(self, request):
        serializer = ReservationChambreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
