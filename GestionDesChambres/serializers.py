from rest_framework import serializers
from .models import Chambre, ReservationChambre


class ChambreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chambre
        fields = "__all__"


class ReservationChambreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationChambre
        fields = "__all__"
