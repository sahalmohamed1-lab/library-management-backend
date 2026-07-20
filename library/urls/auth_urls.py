from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from library.views.auth_views import RegisterAPIView, ProfileAPIView

urlpatterns = [
    # Register
    path(
        "register/",
        RegisterAPIView.as_view(),
        name="register",
    ),

    # Login
    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="login",
    ),

    # Refresh Token
    path(
        "refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
    "profile/",
    ProfileAPIView.as_view(),
    name="profile",
    ),
]