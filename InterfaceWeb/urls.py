# urls.py dans votre application

from django.urls import path
from . import views

urlpatterns = [
    path("statistiques/", views.afficher_statistiques, name="statistiques"),
    # Ajoutez d'autres URLs ici
]
