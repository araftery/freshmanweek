from base import *

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'freshmanweek',
        'USER': 'freshmanweek',
        'PASSWORD': 'freshmanweek',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DEBUG = False
TEMPLATE_DEBUG = False
TIME_ZONE = 'America/New_York'

STATIC_ROOT = '/webapps/freshmanweek/static/'
STATIC_URL = '/static/'

SETTINGS_MODULE = 'freshmanweek.settings.production'

CELERY_RESULT_DBURI = "postgresql://freshmanweek:freshmanweek@localhost/freshmanweek"