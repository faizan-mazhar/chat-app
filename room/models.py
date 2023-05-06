from django.db import models


class ChatRoom(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message = models.TextField()
    sender = models.CharField(max_length=150)
