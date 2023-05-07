# chat/urls.py
from django.urls import path, include

from room.views import SelectRoomView, RoomView


urlpatterns = [
    path("", SelectRoomView.as_view() , name="select_room"),
    path("room/<room>", RoomView.as_view(), name="chat_room"),
    path("api/", include('room.api.v1.urls'))
]