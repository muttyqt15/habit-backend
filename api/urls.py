from django.urls import URLResolver, path, include

urlpatterns = [
    path('auth/', include(('api.authentication.urls', 'auth'))),
]