from django.urls import path
from .views import RechercheChambresAPIView, ReservationChambreAPIView

urlpatterns = [
    path(
        "recherche-chambres/",
        RechercheChambresAPIView.as_view(),
        name="recherche-chambres",
    ),
    path(
        "reservation-chambre/",
        ReservationChambreAPIView.as_view(),
        name="reservation-chambre",
    ),
]
