
from .base import *
import dj_database_url
from decouple import config
import django_heroku


SECRET_KEY = config('SECRET_KEY')
API_KEY = config('API_KEY')
DEBUG = False


###############################################################################
###############################################################################
###############################################################################
#
# Extra Security settings
#
# Enforce Https:
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
os.environ['HTTPS'] = "on"
os.environ['wsgi.url_scheme'] = 'https'

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True
SECURE_HSTS_PRELOAD = True

# Default to 60 minutes
SECURE_HSTS_SECONDS = 3600
#
#
###############################################################################
###############################################################################
###############################################################################

ALLOWED_HOSTS = ['localhost', '*']
COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'assets')
MEDIA_URL = '/assets/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'assets'),
)


# Application definition

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# DB settings
DATABASE_URL = config('DATABASE_URL')
DB_NAME = config('DB_NAME')
DB_PASS = config('DB_PASS')
DB_PORT = config('DB_PORT')
DB_USER = config('DB_USER')

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
# DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}
#
# DB_URL = dj_database_url.parse(DATABASE_URL)


###############################################################################
###############################################################################
###############################################################################
#
# Mailgun Config
#
# EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
# EMAIL_USE_TLS = True
# MAILGUN_API_KEY = config('MAILGUN_API_KEY')
#
# MAILGUN_ACCESS_KEY = config('MAILGUN_ACCESS_KEY')
# MAILGUN_SERVER_NAME = config('MAILGUN_SERVER_NAME')
#
# MAILGUN_DOMAIN = config('MAILGUN_DOMAIN')
# MAILGUN_PUBLIC_KEY = config('MAILGUN_PUBLIC_KEY')
# MAILGUN_SMTP_LOGIN = config('MAILGUN_SMTP_LOGIN')
# MAILGUN_SMTP_PASSWORD = config('MAILGUN_SMTP_PASSWORD')
# MAILGUN_SMTP_PORT = config('MAILGUN_SMTP_PORT')
# MAILGUN_SMTP_SERVER = config('MAILGUN_SMTP_SERVER')
#
###############################################################################
###############################################################################
###############################################################################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
    },
}

# Activate Django-Heroku.
django_heroku.settings(locals())
