# Create your models here.
from django.db import models
from django.conf import settings


class Vol(models.Model):
    numero_vol = models.CharField(max_length=10)
    compagnie_aerienne = models.CharField(max_length=50)
    origine = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    date_depart = models.DateTimeField()
    date_arrivee = models.DateTimeField()
    # Ajoutez d'autres champs nécessaires


class Reservation(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vol = models.ForeignKey(Vol, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(auto_now_add=True)
    # Ajoutez d'autres champs nécessaires
