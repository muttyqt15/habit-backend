from django.contrib.auth.models import AbstractUser
from django.db import models
from core.constants.provider import Provider as prv
from django.db import models
from django.utils import timezone

class ProviderChoices(models.TextChoices):
    GOOGLE = prv.GOOGLE, "GOOGLE"
    GITHUB = prv.GITHUB, "GITHUB"
    DISCORD = prv.DISCORD, "DISCORD"
    NO_PROVIDER = prv.NO_PROVIDER, "NO PROVIDER"

    @classmethod
    def is_provider_valid(cls, provider: str) -> bool:
        for choice in cls.choices:
            if choice[0] == prv.NO_PROVIDER:
                continue

            if provider == choice[0]:
                return True

        return False


class User(AbstractUser):
    email = models.EmailField(unique=True)
    login_provider = models.CharField(
        choices=ProviderChoices.choices,
        max_length=255,
        default=ProviderChoices.NO_PROVIDER,
    )

    def __str__(self):
        return self.username

class RefreshToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="refresh_tokens")
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)

    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return f"Refresh token for {self.user.username} - Expiry: {self.expires_at}"

    def revoke(self):
        self.delete()
