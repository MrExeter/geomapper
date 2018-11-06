'''
Description - WSGI file
@author - John Sentz
@date - 06-Nov-2018
@time - 1:09 PM
'''

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chanfact.settings')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
