# pylint: disable-msg=w0614
from app.settings.base import *

SECRET_KEY = '@q46uxlt0xd-6@*uah76hp^!)5tkrxt!$e_-hr!^^kv+2gy80h'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../data/default.sqlite3'),
    }
}
