# pylint: disable-msg=w0614
from app.settings.base import *

SECRET_KEY = '@q46uxlt0xd-6@*uah76hp^!)5tkrxt!$e_-hr!^^kv+2gy80h'
DEBUG = True
# ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', ''),
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'PORT': os.environ.get('DATABASE_PORT', ''),
    }
}
