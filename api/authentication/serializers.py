from api.authentication.models import User
from rest_framework import serializers


# Serializer for validating and processing user data
class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        # Hash the password before saving
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


# Serializer for validating provider
class SignUpProviderSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        # Hash the password before saving
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


from django.contrib.auth import authenticate
from rest_framework import serializers
from django.core.exceptions import ValidationError


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        # Ensure both email and password are provided
        if not email or not password:
            raise serializers.ValidationError("Email and password are required.")

        # Try to authenticate the user
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid email or password.")

        data["user"] = user
        return data
