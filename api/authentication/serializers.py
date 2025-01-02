from api.authentication.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


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


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        # Ensure both username and password are provided
        if not username or not password:
            raise serializers.ValidationError("Username and password are required.")

        # Try to authenticate the user
        user = authenticate(username=username, password=password)
        
        if user is None:
            raise serializers.ValidationError("Invalid username or password.")

        data["user"] = user
        return data
