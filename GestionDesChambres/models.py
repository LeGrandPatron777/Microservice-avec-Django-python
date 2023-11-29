from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings


class Chambre(models.Model):
    hotel = models.CharField(max_length=100)
    type_chambre = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    # Autres champs selon les données de l'API externe


class ReservationChambre(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(auto_now_add=True)
    date_arrivee = models.DateTimeField()
    date_depart = models.DateTimeField()
    # Autres champs nécessaires pour une réservation
