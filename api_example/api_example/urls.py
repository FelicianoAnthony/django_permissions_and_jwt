"""api_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # Access & refresh token 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('languages.urls')),
    path('api-auth/', include('rest_framework.urls')), # gives a login on top right corner of page
    path('api/token/', TokenObtainPairView.as_view()), # use as_view() for classes
    path('api/token/refresh/', TokenRefreshView.as_view())
]
