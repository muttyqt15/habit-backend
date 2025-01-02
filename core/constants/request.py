from typing import Any
from django.contrib.auth.models import AnonymousUser
from api.authentication.models import User


class RequestBody:
    def get(self, key: str, default: Any = ...) -> Any: ...


class Request:
    data: RequestBody
    user: AnonymousUser | User
