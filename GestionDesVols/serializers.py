from rest_framework import serializers
from .models import Vol, Reservation


class VolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vol
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
