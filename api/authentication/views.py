from rest_framework import authentication, response, views, status
from rest_framework.permissions import AllowAny
from api.authentication.serializers import SignUpSerializer, LoginSerializer
from api.authentication.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from core.constants.request import Request


# APIView for handling user registration
class SignUpView(views.APIView):
    permission_classes = [AllowAny]  # Allow anyone to access this endpoint

    def post(self, request) -> response.Response:
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return response.Response(
                {"message": "User created successfully.", "username": user.username},
                status=status.HTTP_201_CREATED,
            )
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignUpProviderView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request) -> response.Response:
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return response.Response(
                {"message": "User created successfully.", "username": user.username},
                status=status.HTTP_201_CREATED,
            )
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# APIView for handling user login
class LoginView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request) -> response.Response:
        print("hi")
        print(request.data)
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(email=request.data.get("email"))
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            return response.Response(
                {
                    "message": "User logged in successfully.",
                    "data": {
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                        "username": user.username,
                    },
                },
                status=status.HTTP_201_CREATED,
            )
        print(request)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
