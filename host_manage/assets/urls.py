from django.urls import path
from .views import create_host, ping_host

urlpatterns = [
    path('host/', create_host),
    path('host/<int:host_id>/ping/', ping_host),
]
