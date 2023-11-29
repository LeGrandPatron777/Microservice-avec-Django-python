from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vol, Reservation
from .serializers import VolSerializer, ReservationSerializer
import requests


class RechercheVolsAPIView(APIView):
    def get(self, request):
        # Remplacez par l'URL de l'API REST externe
        response = requests.get("https://api.externe/vols/")
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
