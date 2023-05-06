from django.contrib import admin
from room.models import ChatRoom, Message

admin.site.register(ChatRoom)
admin.site.register(Message)