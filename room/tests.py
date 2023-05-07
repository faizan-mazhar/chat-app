from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from project.utils import BaseTest
from room.models import ChatRoom

class ChatRoomTest(BaseTest, TestCase):
    template_name = 'room/index.html'
    testing_view = 'select_room'
    login_view = 'login'

    def get_post_data(self):
        return {"name": "Test room"}
    
    def extra_get_checks(self, response):
        self.assertEqual(len(response.context_data["rooms"]), 0)
    
    def extra_post_test(self, post_data):
        self.assertTrue(ChatRoom.objects.filter(name=post_data["name"]).exists())

    def get_success_url(self):
        data = self.get_post_data()
        return reverse('chat_room', args=[data["name"]])

class RoomViewTest(BaseTest, TestCase):
    template_name = 'room/room.html'
    testing_view = 'chat_room'
    login_view = 'login'

    def setUp(self):
        super().setUp()
        self.room_name = "testing"

    def get_view_url(self):
        return reverse(self.testing_view, args=[self.room_name])

    def extra_get_checks(self, response):
        self.assertEqual(response.context_data["messages"], "[]")
        self.assertEqual(response.context_data["room_name"], self.room_name)
    
    def test_post_request(self):
        '''
            This view does not implement POST method
        '''
        pass

