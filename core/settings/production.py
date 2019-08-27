from .base import *

DEBUG = False

ALLOWED_HOSTS = ['ip-address', 'wwww.plunder.com']


# Postgresql Settings
DATABASES = {
    'default': {
        'ENGINE': config(ENGINE),
        'NAME': config(NAME),
        'USER': config(USER),
        'PASSWORD': config(PASSWORD),
        'HOST': config(HOST),
        'PORT': config(PORT),
    }
}
