from django.shortcuts import render

# Create your views here.
# views.py

import requests


def afficher_statistiques(request):
    reponse = requests.get("url_du_microservice")
    statistiques = reponse.json()
    return render(
        request,
        "nom_de_votre_application/statistiques.html",
        {"statistiques": statistiques},
    )
