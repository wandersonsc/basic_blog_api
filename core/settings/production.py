from .base import *

DEBUG = False

ALLOWED_HOSTS = ['ip-address', 'http://127.0.0.1:8000/api/v1/']


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
