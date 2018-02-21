import os
import dj_database_url

from .base import *

ALLOWED_HOSTS = ['davidhousedev-boston-westie.herokuapp.com']

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'] = db_from_env

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
