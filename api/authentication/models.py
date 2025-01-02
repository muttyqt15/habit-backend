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
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username