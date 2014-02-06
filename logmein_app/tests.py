import datetime
import unittest
import time
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import Client
from .views import LogmeinBackend


class LogmeinTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logmein_backend = LogmeinBackend()
        cls.client = Client()
        User.objects.all().delete()
        User.objects.create_superuser('root', u'r@r.com', '1234', pk=100)

    @classmethod
    def get_token(cls):
        second = datetime.datetime.now().second
        return cls.logmein_backend.get_token(second)

    def test_can_login(self):
        """Can login with a valid token"""
        token = self.get_token()
        self.assertTrue(self.logmein_backend.authenticate(token=token))

    def test_cant_login_with_random_token(self):
        """Cant login with a random token"""
        token = '9207a1b6b91614e110b606fa6096ace4c22dd83e743f6c600ce0a1d5'
        self.assertFalse(self.logmein_backend.authenticate(token=token))

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
        token_param = '?token=%s' % (self.get_token(), )
        login_url = ''.join([reverse('logmein_login'), token_param])
        response = self.client.get(login_url)
        self.assertTrue(response.cookies.get('sessionid'))

    def test_user_shouldnt_be_loged_when_token_is_invalid(self):
        """User shouldnt be loged if token is invalid"""
        token_param = '?token=%s' % ('AISHCAIUHCUASICuihiuihiuhuihi98989', )
        login_url = ''.join([reverse('logmein_login'), token_param])
        response = self.client.get(login_url)
        self.assertFalse(response.cookies.get('sessionid'))

    def test_backend_should_return_user_given_a_pk(self):
        """Backend should return user given a pk"""
        user = self.logmein_backend.get_user(user_id=100)
        self.assertTrue(user)


if __name__ == '__main__':
    unittest.main()
