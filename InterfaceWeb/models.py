from django.db import models

# Create your models here.


class Statistique(models.Model):
    nom = models.CharField(max_length=100)
    valeur = models.FloatField()

    def __str__(self):
        return self.nom
