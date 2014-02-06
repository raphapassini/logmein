logmein_app
===========

A client to remote login system for django.
See: https://github.com/raphapassini/logmein

Installing the client
---------------------

* Active your project [virtualenv](https://pypi.python.org/pypi/virtualenv), for example purposes i'll use ```django_project```
  I'm also considering that you're using [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)

```
$ workon django_project
$ cd /path/to/django_project
```

* Install **logmein_app** inside your project virtualenv

```
$ pip install logmein_app
```

* Inside the **django_project** alter the ```urls.py```

```
import logmein_app

urlpatterns = patterns(
    '',
    [...suppressed code]
    url(r'^logmein/', include('logmein_app.urls')),
)
```

* Also alter the ```settings.py```

```
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'logmein_app.views.LogmeinBackend',
)
```
