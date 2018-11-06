from .base import *
from settings_secret import *

DEBUG = True

SECRET_KEY = "lkcoirkglpds0eolkflvf566454agflskdjflskdjfoawisjalskdjl;kjw45kmsgdfmks'kg"
API_KEY = API_KEY

MEDIA_ROOT = os.path.join(BASE_DIR, 'assets')
MEDIA_URL = '/assets/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'assets'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'chanfact_dev_db',
        'USER': 'dbdeveloper',
        'PASSWORD': 'dbdeveloper',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}

# For Development ONLY!   run   python -m smtpd -n -c DebuggingServer localhost:1025 in separate terminal
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
DEFAULT_FROM_EMAIL = 'No Reply <noreply@jtsinteractive.com>'


DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}

print("Static Files Dirs = {}".format(STATICFILES_DIRS))
print("Static Root".format(STATIC_ROOT))
