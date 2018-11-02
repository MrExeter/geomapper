from .base import *
from settings_secret import *

# DEBUG = True
DEBUG = True

# STATIC_ROOT = "/Users/johnsentz/Documents/Software_Projects/Python/Commercial_Projects/STARGEN/bgc_dj_stargen/static/"
# MEDIA_ROOT = "/Users/johnsentz/Documents/Software_Projects/Python/Commercial_Projects/STARGEN/bgc_dj_stargen/static/"
SECRET_KEY = "lkcoirkglpds0eolkflvf566454agflskdjflskdjfoawisjalskdjl;kjw45kmsgdfmks'kg"
API_KEY = API_KEY
# API_KEY = config('API_KEY')
# STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# STATIC_ROOT = 'static'
MEDIA_ROOT = os.path.join(BASE_DIR, 'assets')
MEDIA_URL = '/assets/'
STATIC_URL = '/static/'
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )
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
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
DEFAULT_FROM_EMAIL = 'No Reply <noreply@jtsinteractive.com>'
# MAILGUN_SMTP_SERVER = config('MAILGUN_SMTP_SERVER')
# MAILGUN_SMTP_PORT = config('MAILGUN_SMTP_PORT')
# MAILGUN_SMTP_LOGIN = config('MAILGUN_SMTP_LOGIN')
# MAILGUN_SMTP_PASSWORD = config('MAILGUN_SMTP_PASSWORD')
# EMAIL_USE_TLS = True


DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}

print("Static Files Dirs = {}".format(STATICFILES_DIRS))
print("Static Root".format(STATIC_ROOT))
