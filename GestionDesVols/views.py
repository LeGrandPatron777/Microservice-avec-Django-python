from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vol, Reservation
from .serializers import VolSerializer, ReservationSerializer
import requests
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


class RechercheVolsAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Recherche de vols",
        manual_parameters=[
            openapi.Parameter(
                "origin",
                openapi.IN_QUERY,
                description="Origine du vol",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "destination",
                openapi.IN_QUERY,
                description="Destination du vol",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "depart_date",
                openapi.IN_QUERY,
                description="Date de départ",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "return_date",
                openapi.IN_QUERY,
                description="Date de retour",
                type=openapi.TYPE_STRING,
            ),
        ],
    )
    def get(self, request):
        # Récupérer les paramètres de la requête
        origine = request.query_params.get("origin")
        destination = request.query_params.get("destination")
        depart_date = request.query_params.get("depart_date")
        return_date = request.query_params.get("return_date")

        # Vérifier que les paramètres nécessaires sont présents
        if not origine or not destination or not depart_date or not return_date:
            return Response({"error": "Paramètres manquants"}, status=400)

        # Construire l'URL avec les paramètres
        url = f"https://api.travelpayouts.com/v1/prices/cheap?origin={origine}&destination={destination}&depart_date={depart_date}&return_date={return_date}&token=6ccf4da559f0777e5a5c543cd67ca555"

        # Effectuer la requête à l'API externe
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())
        else:
            return Response(response.text, status=response.status_code)


class ReservationAPIView(APIView):
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
