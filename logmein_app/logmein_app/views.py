import datetime
import hashlib
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden
from django.conf import settings
from .security import DecodeAES


class LogmeinBackend(object):

    def check_token(self, user_token, limit_seconds=30):
        second = datetime.datetime.now().second
        for i in range(limit_seconds + 1):
            token = self.get_token(second=(second - i))
            if token == user_token:
                return True
        return False

    def get_token(self, second=False):
        now = datetime.datetime.utcnow()
        if not second:
            second = now.second

        token_str = ''.join(
            [settings.SECRET_KEY, now.strftime("%Y%m%d%H%M"), str(second), ])

        token = hashlib.sha224(token_str).hexdigest()
        return token

    def authenticate(self, username, token):
        username = DecodeAES(username)
        user = None
        if self.check_token(user_token=token):
            user = User.objects.get(username=username)
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def logmein_login(request):
    if request.GET.get('gen') and settings.DEBUG:
        print LogmeinBackend().get_token()

    username = request.GET.get('username')
    token = request.GET.get('token')
    try:
        user = authenticate(username=username, token=token)
    except User.DoesNotExist:
        return HttpResponseForbidden('Invalid username')

    if user is not None:
        login(request, user)
    return redirect('admin:index')
