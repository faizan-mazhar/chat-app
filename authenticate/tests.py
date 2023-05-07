from django.urls import reverse
from django.test import TestCase

from project.utils import BaseTest

class ChatRoomTest(BaseTest, TestCase):
    template_name = 'auth/login.html'
    testing_view = 'login'

    def get_post_data(self):
        return {"username": self.user.username, "password": self.user_pass}
    
    def get_success_url(self):
        return reverse('select_room')

    def test_get_request_without_login(self):
        '''
            This is a public view.
        '''
        pass


class UserCreateViewTest(BaseTest, TestCase):
    template_name = 'auth/register.html'
    testing_view = 'register'

    def get_post_data(self):
        return { "username": "test_user", "password1": "TestPass!23", "password2": "TestPass!23"}

    def get_success_url(self):
        return reverse('login')

    def test_get_request_without_login(self):
        '''
            This is a public view.
        '''
        pass