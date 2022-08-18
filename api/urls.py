from django.urls import path
from api.views import get_webhook

urlpatterns = [
    path('webhook', get_webhook),
]
