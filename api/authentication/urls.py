from django.urls import URLResolver, path, include
from api.authentication.views import SignUpView, SignUpProviderView, LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("sign-up/", SignUpView.as_view()),
    path("sign-up/<str:provider>", SignUpProviderView.as_view()),
    path("login/", LoginView.as_view()),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
