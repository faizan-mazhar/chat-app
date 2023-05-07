from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from room.api.v1.serializers import ChatRoomSerializer, MessageSerializer
from room.models import ChatRoom, Message


class ChartRoomListAPI(ListAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [IsAuthenticated]


class MessageListAPI(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        room_name = self.kwargs.get("room")
        return Message.objects.filter(room__name=room_name)
