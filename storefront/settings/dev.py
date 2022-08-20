from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-=0fb)vaco33nnx%!=^_9x1637ky$d@au4)-j=^%n&f759skzdt'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mosh_tutorial3',
        'HOST': 'localhost',
        'USER': 'kate',
        'PASSWORD': 'cateobi'
    }
}