from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings


class Facture(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()
    # Autres champs nécessaires eeeeeeeeeeeee
