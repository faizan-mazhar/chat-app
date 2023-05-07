from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient

User = get_user_model()

class BaseTest:
    '''
        BaseTest is base test class which provides basic implementation for common checks. 

        Attributes:
        template_name: Template name used by view. Template is checked for a successful get request
        testing_view: View path name which is being tested by test suite
        login_view: Login view path name. This is used to check if unauthorize user gets reidrect to login view
        user: User used to login during testing
        user_pass: User password for testing purpose
    '''
    template_name = None
    testing_view = None
    login_view = None
    user = None
    user_pass = None

    def setUp(self):
        self.user_pass = "12345"
        self.user = User.objects.create_user(username="test", password=self.user_pass)
    
    def login_client(self):
        # force login because login takes longer since it has to verify everything
        # and run through all the checks
        self.client.force_login(self.user)
    
    def get_view_url(self):
        '''
            Helper method used to rever a view name into path
        '''
        return reverse(self.testing_view)

    def get_login_url(self):
        '''
            Helper method used to generate redirect url for login required method
        '''
        return f"{reverse(self.login_view)}?next={self.get_view_url()}"

    def test_get_request_without_login(self):
        '''
            Test if unauthorized user gets reidrected to the login page
        '''
        response = self.client.get(self.get_view_url())
        self.assertRedirects(response, self.get_login_url())
    
    def test_get_request_with_login(self):
        '''
            Test if authorized user is able to access the page
        '''
        self.login_client()
        response = self.client.get(self.get_view_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_name)
        self.extra_get_checks(response)
    
    def test_post_request(self):
        '''
            To test if new room is created and user gets reidrected to room view
        '''
        data = self.get_post_data()
        self.login_client()
        response = self.client.post(self.get_view_url(), data=data)
        self.assertRedirects(response, self.get_success_url())
        self.extra_post_test(data)

    def get_success_url(self):
        '''
            Helper method to get success url for post request
        '''
        pass
    def get_post_data(self):
        '''
            Helper method to provide data for post requeset
        '''
        pass

    def extra_post_test(self, post_data):
        '''
            Method to perform extra post test for veritfication
            params:
            post_data: Data which was used to make post request is passed through this parameter
        '''
        pass

    def extra_get_checks(self, response):
        '''
            Method to perform extra post test for veritfication
            params:
            response: Response from client get request to the view
        '''
        pass


class APITestBase:
    view_path_name = None

    def setUp(self):
        super().setUp()
        self.client = APIClient()
        self.user_pass = "12345"
        self.user = User.objects.create_user(username="test", password=self.user_pass)

    def authenticate_client(self):
        self.client.force_login(self.user)

    def get_view_url(self):
        return reverse(self.view_path_name)

    def get_test_data(self):
        pass

    def test_get_without_login(self):
        response = self.client.get(self.get_view_url())
        self.assertEqual(response.status_code, 403)

    def test_get_with_login(self):
        self.authenticate_client()
        response = self.client.get(self.get_view_url())
        reponse_data = self.get_test_data()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, reponse_data)
