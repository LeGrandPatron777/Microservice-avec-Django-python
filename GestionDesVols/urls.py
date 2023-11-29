from django.urls import path
from .views import RechercheVolsAPIView, ReservationAPIView

urlpatterns = [
    path("recherche/", RechercheVolsAPIView.as_view(), name="recherche-vols"),
    path("reservation/", ReservationAPIView.as_view(), name="reservation"),
]
