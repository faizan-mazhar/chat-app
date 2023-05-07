import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer
from room.models import ChatRoom, Message
from room.api.v1.serializers import ClientMessageSerializer


class ChatConsumer(AsyncWebsocketConsumer):

    @database_sync_to_async
    def get_room_object_refernce(self):
        self.room = ChatRoom.objects.get(name=self.room_name)

    @database_sync_to_async
    def store_message(self, message, user_id):
        Message.objects.create(room=self.room, message=message, sender=user_id)

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.sanatized_room_name = self.room_name.replace(" ", "_")
        self.room_group_name = f"group_{self.sanatized_room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.get_room_object_refernce() # get current room id to store message
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user_id = text_data_json["user_id"]
        await self.store_message(message, user_id)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, "user_id": user_id}
            )

    async def chat_message(self, event):
        message = event["message"]
        user_id = event["user_id"]
        await self.send(text_data=json.dumps({"message": message, "user_id": user_id}))


class ChatConsumerAPI(AsyncJsonWebsocketConsumer):
    
    @database_sync_to_async
    def get_room_object_refernce(self):
        self.room = ChatRoom.objects.get(name=self.room_name)

    @database_sync_to_async
    def store_message(self, message, user_id):
        Message.objects.create(room=self.room, message=message, sender=user_id)

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.sanatized_room_name = self.room_name.replace(" ", "_")
        self.room_group_name = f"group_{self.sanatized_room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.get_room_object_refernce() # get current room id to store message
        await self.accept()
    
    async def receive_json(self, content, **kwargs):
        '''
        This will handle messages sent over the network from client
        '''
        serializer = ClientMessageSerializer(data=content)

        if not serializer.is_valid():
            return
        
        await self.store_message(serializer.data['message'], serializer.data['user_id'])

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "content": serializer.data}
        )

    async def chat_message(self, event):
        await self.send_json(event["content"])

