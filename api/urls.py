from django.urls import path
from .views import ReturnsAPI

urlpatterns = [
    path('returns/', ReturnsAPI.as_view(), name = 'returns_api'),
]