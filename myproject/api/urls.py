from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, home, logout_view

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('api/', include(router.urls)), 
]