from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')), 
    # path('', lambda request: redirect('/api/users/', permanent=True)),  # Redirect base URL to /api/users/
    path('accounts/', include('allauth.urls'))
]


