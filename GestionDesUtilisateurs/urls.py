from django.urls import path
from .views import CreateUserView, UpdateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("create_user/", CreateUserView.as_view(), name="create_user"),
    path("update_user/<int:pk>/", UpdateUserView.as_view(), name="update_user"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
