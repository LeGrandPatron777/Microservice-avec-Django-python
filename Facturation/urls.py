from django.urls import path
from .views import PaiementAPIView

urlpatterns = [
    path("paiement/", PaiementAPIView.as_view(), name="paiement"),
    # Ajoutez d'autres chemins d'URL au besoin
]
