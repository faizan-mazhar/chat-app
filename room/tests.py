from django.test import TestCase
from django.urls import reverse


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


    def test_chat_consumer(self):
        @transaction.atomic
        async def test_chat():
            communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), '/ws/chat/test/')
            connected, _ = await communicator.connect(timeout=10)
            self.assertTrue(connected)

            data = {
                'message': 'Testing',
                'user_id': '3',
            }
            await communicator.send_json_to(data)

            response = await communicator.receive_json_from()
            self.assertEqual(response['message']['text'], 'Testing')
            self.assertEqual(response['message']['user_name'], '3')

            # chat_message = await sync_to_async(ChatMessage.objects.filter)(chat_room=self.chat_room, message=message,
            #                                                                user=self.user)
            # self.assertIsNotNone(chat_message)

            await communicator.disconnect()

        # Call async function from sync context
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(test_chat())