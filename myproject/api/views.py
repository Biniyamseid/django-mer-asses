from django.shortcuts import render, redirect
from django.contrib.auth import logout
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer, UserRegistrationSerializer

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect("/")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegistrationSerializer
        return UserSerializer