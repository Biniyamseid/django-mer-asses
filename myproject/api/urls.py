# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet

# router = DefaultRouter()
# router.register(r'users', UserViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
#     path('accounts/', include('allauth.urls')),
# ]
# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, include the allauth URLs for social authentication.
urlpatterns = [
    path('', include(router.urls)),  # Use an empty string for the router base
    path('accounts/', include('allauth.urls')),
]
