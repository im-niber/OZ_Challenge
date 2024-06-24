from django.urls import re_path, path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<int:room_id>/', ChatConsumer.as_wsgi())
]