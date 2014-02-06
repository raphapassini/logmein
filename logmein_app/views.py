import datetime
import hashlib
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.conf import settings


class LogmeinBackend(object):
    root_username = 'root'

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

    def authenticate(self, token=None):
        user = None
        if self.check_token(user_token=token):
            try:
                user = User.objects.get(username=self.root_username)
            except User.DoesNotExist:
                pass
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def logmein_login(request):
    print datetime.datetime.utcnow()
    if request.GET.get('gen') and DEBUG:
        print LogmeinBackend().get_token()

    user = authenticate(token=request.GET.get('token'))
    if user is not None:
        login(request, user)
    return redirect('admin:index')
