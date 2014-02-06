Logmein
=======

A remote login system for django. Control your "root" user in several projects in a single place, you can login with just 1 click.

You have to manage your "root" login over several projects? The aim of this project is provide a simple interface where you can centralize all your projects and connect with just one click.

Installing the client
---------------------

* First clone **Logmein** project

```
$ git clone https://github.com/raphapassini/logmein.git
$ cd logmein/
```

* Active your project [virtualenv](https://pypi.python.org/pypi/virtualenv), for example purposes i'll use ```django_project```.  
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

* Now you're done with the client setup!


Installing the Logmein Admin
----------------------------

* Install the requirements

```
$ cd /path/to/logmein/folder/logmein_adm/
$ pip install -Mr requirements.txt
```

* Configure production settings in ```project/prod_settings.py```

```
DEBUG = TEMPLATE_DEBUG = False

ADMINS = (
    # ('Admin User', 'admin@user.com'),
)

MANAGERS = ADMINS
ALLOWED_HOSTS = ['http://mydomain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'logmein_adm',
        'USER': 'root',
        'PASSWORD': 'super_secret_password',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_ROOT = '/var/www/logmein_adm/media/'
MEDIA_URL = '/media/'

STATIC_ROOT = '/var/www/logmein_adm/static/'
STATIC_URL = '/static/'
```

* Sync DB and migrate

```
$ python manage.py syncdb
$ python manage.py migrate --all
```

* Finish! Now you can run **logmein_adm** and start to insert your projects.  
  If you're intent to use the **logmein_adm** locally you can start the server by typing
```
$ python manage.py runserver
```

IMPORTANT NOTES
-------------------

* You'll need the secret off every remote client you want to connect to, the secret is stored in ```SECRET_KEY``` inside   the ```settings.py```

TODO
----

* Write tests to logmein_adm
* Think a better way to validate the token ( the token should be valid at max for 30secs )
* Have a suggestion? Mail me at raphapassini [at] gmail [dot] com
