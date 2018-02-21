import os

from .base import *

ALLOWED_HOSTS = ['davidhousedev-boston-westie.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB_NAME'],
        'USER': os.environ['POSTGRES_USER'],
        'HOST': os.environ['DATABASE_URL'],
        'PORT': 5432,
    }
}

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
