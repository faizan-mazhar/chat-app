import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_name = self.room_name.replace(" ", "_")
        self.room_group_name = f"group_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user_id = text_data_json["user_id"]
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, "user_id": user_id}
            )

    async def chat_message(self, event):
        print("event")
        message = event["message"]
        user_id = event["user_id"]
        await self.send(text_data=json.dumps({"message": message, "id": user_id}))
