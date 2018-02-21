import os

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '.ngrok.io']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}