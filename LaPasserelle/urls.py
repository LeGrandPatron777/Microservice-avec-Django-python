# passerelle/urls.py

from django.urls import path, include

urlpatterns = [
    # Inclure les URLs des microservices
    path("Utilisateurs/", include("GestionDesUtilisateurs.urls")),
    path("Vols/", include("GestionDesVols.urls")),
    path("Chambres/", include("GestionDesChambres.urls")),
    path("Paiment et Facturation/", include("Facturation.urls")),
    # Vous pouvez ajouter d'autres microservices ici
]
