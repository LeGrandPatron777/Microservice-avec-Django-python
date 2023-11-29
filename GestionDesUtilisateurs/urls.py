from django.urls import path
from .views import CreateUserView, UpdateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("inscription/", CreateUserView.as_view(), name="create_user"),
    path("mise-a-jour/<int:pk>/", UpdateUserView.as_view(), name="update_user"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
