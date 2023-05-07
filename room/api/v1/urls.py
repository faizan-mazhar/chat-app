from django.urls import path

from room.api.v1.viewsets import ChartRoomListAPI, MessageListAPI


urlpatterns = [
    path("chat/room/", ChartRoomListAPI.as_view(), name="api_chat_room"),
    path("message/<room>/", MessageListAPI.as_view(), name="api_message"),
]

