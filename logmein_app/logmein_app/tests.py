import datetime
import unittest
import time
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import Client
from .views import LogmeinBackend
from .security import EncodeAES


class LogmeinTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logmein_backend = LogmeinBackend()
        cls.client = Client()
        cls.username = EncodeAES('root')
        User.objects.all().delete()
        User.objects.create_superuser('root', u'r@r.com', '1234', pk=100)

    @classmethod
    def get_token(cls):
        second = datetime.datetime.now().second
        return cls.logmein_backend.get_token(second)

    def test_can_login(self):
        """Can login with a valid token"""
        token = self.get_token()
        self.assertTrue(
            self.logmein_backend.authenticate(username=self.username,
                                              token=token))

    def test_cant_login_with_random_token(self):
        """Cant login with a random token"""
        token = '9207a1b6b91614e110b606fa6096ace4c22dd83e743f6c600ce0a1d5'
        self.assertFalse(
            self.logmein_backend.authenticate(username=self.username,
                                              token=token))

    def test_cant_login_with_expired_token(self):
        """Cant login with a expired token"""
        token = self.get_token()
        time.sleep(2)  # wait 2 seconds, so the token will expire
        self.assertFalse(self.logmein_backend.check_token(user_token=token,
                                                          limit_seconds=1))

    def test_token_should_be_valid_for_x_seconds(self):
        """Token should be valid for X seconds"""
        token = self.get_token()
        time.sleep(3)
        self.assertTrue(self.logmein_backend.check_token(user_token=token,
                                                         limit_seconds=4))

    def test_user_should_be_loged_when_token_is_valid(self):
        """User should be loged if token is valid"""
        url_params = '?token=%s&username=%s' % (self.get_token(),
                                                self.username)
        login_url = ''.join([reverse('logmein_login'), url_params])
        self.client.get(login_url)
        self.assertTrue(self.client.session.get('_auth_user_id'))

    def test_user_shouldnt_be_loged_when_token_is_invalid(self):
        """User shouldnt be loged if token is invalid"""
        username = EncodeAES('john_doe')
        token_param = '?token=%s&username=%s' %\
            ('AISHCAIUHCUASICuihiuihiuhuihi98989', username)
        login_url = ''.join([reverse('logmein_login'), token_param])
        self.client.logout()
        self.client.get(login_url)
        self.assertFalse(self.client.session.get('_auth_user_id'))

    def test_user_shouldnt_be_loged_when_username_doesnt_exist(self):
        """User shouldnt be loged if username doesnt exist"""
        username = EncodeAES('john_doe')
        url_params = '?token=%s&username=%s' % (self.get_token(),
                                                username)
        login_url = ''.join([reverse('logmein_login'), url_params])
        self.client.logout()
        response = self.client.get(login_url)
        self.assertTrue(response.status_code == 403)

    def test_backend_should_return_user_given_a_pk(self):
        """Backend should return user given a pk"""
        user = self.logmein_backend.get_user(user_id=100)
        self.assertTrue(user)


if __name__ == '__main__':
    unittest.main()
