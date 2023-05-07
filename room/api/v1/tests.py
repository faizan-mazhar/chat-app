from django.urls import reverse
from django.test import TestCase
from room.api.v1.serializers import ChatRoomSerializer
from room.models import ChatRoom
from project.utils import APITestBase


class TestChartRoomListAPI(APITestBase, TestCase):
    view_path_name = 'api_chat_room'

    def get_test_data(self):
        serialzier = ChatRoomSerializer(ChatRoom.objects.all(), many=True)
        return serialzier.data


class TestMessageListAPI(APITestBase, TestCase):
    view_path_name = 'api_message'

    def get_view_url(self):
        return reverse(self.view_path_name, args=['testing'])
    
    def get_test_data(self):
        return []