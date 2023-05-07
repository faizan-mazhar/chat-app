from django.urls import path

from room.consumers import ChatConsumer, ChatConsumerAPI

websocket_urlpatterns = [
    path("ws/chat/<room_name>/", ChatConsumer.as_asgi(), name="ws_chat_socket"),
    path("ws/chat/api/<room_name>/", ChatConsumerAPI.as_asgi(), name="ws_chat_api_socket")
]