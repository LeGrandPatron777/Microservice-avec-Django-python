from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Chambre, ReservationChambre
from .serializers import ChambreSerializer, ReservationChambreSerializer
import requests


class RechercheChambresAPIView(APIView):
    def get(self, request):
        # Ici, faites une requête à l'API externe
        response = requests.get("URL_API_EXTERNE_CHAMBRES")
        if response.status_code == 200:
            # Traiter et renvoyer les données
            return Response(response.json())
        return Response(response.text, status=response.status_code)


class ReservationChambreAPIView(APIView):
    def post(self, request):
        serializer = ReservationChambreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
