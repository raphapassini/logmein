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

* Move the ```logmein_app``` foder to the project we want to remotely connect.  
  For example purposes we gonna call this project **django_project**

```
$ cp logmein_app /path/to_my/django_project/
```

* Inside the **django_project** alter the ```urls.py```

```
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

* Finish! Now you can run **logmein_adm** and start to insert your projects
  If you're intent to use the **logmein_adm** locally you can start the server by typing
```
$ python manage.py runserver
```

IMPORTANT NOTES
-------------------

* You'll need the secret off every remote client you want to connect to, the secret is stored in ```SECRET_KEY``` inside   the ```settings.py```

TOOD
----

* Write tests to logmein_adm
* Think a better way to validate the token ( the token should be valid at max for 30secs )
* Any suggestion? Mail me at raphapassini [at] gmail [dot] com
