from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path("ws/scoket-server/", consumers.ChatConsumer.as_asgi(), name="chat_consumer")
    
]