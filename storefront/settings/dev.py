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

CELERY_BROKER_URL = 'redis://localhost:6379/1'
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "TIMEOUT": 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525
DEFAULT_FROM_EMAIL = 'akinyi180@gmail.com'