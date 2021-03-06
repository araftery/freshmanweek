from datetime import timedelta
import os

from path import path

############################################################
##### SETUP ################################################
############################################################

# i.e., where root urlconf is
PROJECT_ROOT = path(__file__).abspath().dirname().dirname()
os.sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))


############################################################
##### DATABASE #############################################
############################################################

ALLOWED_HOSTS = ['*']

############################################################
##### APPS #################################################
############################################################

# Application definition
DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)

THIRD_PARTY_APPS = (
    'south',
    'gunicorn',
    'widget_tweaks',
    'dbbackup',
    'compressor',
    'crispy_forms',
    'localflavor',
    'djrill',
    'djcelery',
)

MY_APPS = (
    'core',
    'talentshow',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + MY_APPS

############################################################
##### MIDDLEWARE ###########################################
############################################################

DEFAULT_MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

THIRD_PARTY_MIDDLEWARE = (
)

MIDDLEWARE_CLASSES = DEFAULT_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE

############################################################
##### INTERNATIONALIZATION #################################
############################################################

LANGUAGE_CODE = 'en-us'
USE_I18N = False
USE_L10N = False
INTERNAL_IPS = ['*']

############################################################
##### TEMPLATES ############################################
############################################################

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates_common').replace('\\','/'),
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as DEFAULT_TCP

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'core.context_processors.debug',
    'core.context_processors.is_it_freshmanweek',
    'core.context_processors.site_url',
) + DEFAULT_TCP


############################################################
##### AUTHENTICATION #######################################
############################################################

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
URL_PATH = ''

############################################################
##### EMAIL ################################################
############################################################

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
FROM_EMAIL = os.environ.get('FROM_EMAIL')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT')

try:
    EMAIL_PORT = int(EMAIL_PORT)
except ValueError:
    pass

ADMINS = (
    ('Andrew Raftery', 'andrewraftery@gmail.com'),
)

EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
HARVARD_TALENT_EMAIL = 'Harvard Talent Show 2019 <harvardtalent19@gmail.com>'
HARVARD_TALENT_EMAIL_ADDRESS = 'harvardtalent19@gmail.com'
DEFAULT_FROM_EMAIL = HARVARD_TALENT_EMAIL
MANDRILL_API_KEY = os.environ.get('MANDRILL_API_KEY')

############################################################
##### STATIC FILES #########################################
############################################################

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static_common').replace('\\','/'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)
COMPRESS_CSS_FILTERS = (
     'compressor.filters.cssmin.CSSMinFilter',
)


############################################################
##### OTHER ################################################
############################################################

ROOT_URLCONF = 'freshmanweek.urls'
WSGI_APPLICATION = 'freshmanweek.wsgi.application'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
SECRET_KEY = 'ye#fv=lsp5sm@4lg@23(55d64qydp1%=2)wdkr!twr5_827g8n'
DATABASES = {}
TIME_ZONE = 'America/New_York'
USE_TZ = True
SITE_ID = 1

############################################################
##### CRISPY FORMS  ########################################
############################################################

CRISPY_TEMPLATE_PACK = 'bootstrap3'

############################################################
##### PROJECT-SPECIFIC #####################################
############################################################

TWILIO_PHONE_NUMBER = '+16172998450'
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

FWK_START_DATE = (2015, 8, 24, 0, 0)
#IS_FWK = True


CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
BROKER_URL = "amqp://freshmanweek:freshmanweek@localhost:5672/freshmanweek"
CELERY_RESULT_DBURI = "postgresql://freshmanweek:freshmanweek@localhost/freshmanweek"
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = TIME_ZONE

# put these two lines at the very bottom of the settings file
import djcelery
djcelery.setup_loader()
