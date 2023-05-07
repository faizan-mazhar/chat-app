from rest_framework import serializers
from room.models import Message, ChatRoom


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = "__all__"


class ClientMessageSerializer(serializers.Serializer):
    message = serializers.CharField()
    user_id = serializers.CharField()