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
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

THIRD_PARTY_MIDDLEWARE = (
)

MIDDLEWARE_CLASSES = DEFAULT_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE

############################################################
##### INTERNATIONALIZATION #################################
############################################################

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'US/Eastern'
USE_I18N = False
USE_L10N = False
USE_TZ = True
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
) + DEFAULT_TCP


############################################################
##### AUTHENTICATION #######################################
############################################################

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
URL_PATH = ''

############################################################
##### AWS ##################################################
############################################################

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

############################################################
##### EMAIL ################################################
############################################################

MANDRILL_USER = os.environ.get('MANDRILL_USER')
MANDRILL_API_KEY = os.environ.get('MANDRILL_API_KEY')
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

ADMINS = (
    ('Andrew Raftery', 'andrewraftery@gmail.com'),
)


############################################################
##### DB BACKUPS ###########################################
############################################################

DBBACKUP_STORAGE = 'dbbackup.storage.s3_storage'
DBBACKUP_S3_BUCKET = AWS_STORAGE_BUCKET_NAME
DBBACKUP_S3_ACCESS_KEY = AWS_ACCESS_KEY_ID
DBBACKUP_S3_SECRET_KEY = AWS_SECRET_ACCESS_KEY

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


############################################################
##### OTHER ################################################
############################################################

ROOT_URLCONF = 'freshmanweek.urls'
WSGI_APPLICATION = 'freshmanweek.wsgi.application'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
SECRET_KEY = 'ye#fv=lsp5sm@4lg@23(55d64qydp1%=2)wdkr!twr5_827g8n'
DATABASES = {}
TIME_ZONE = 'America/New_York'

############################################################
##### CRISPY FORMS  ########################################
############################################################

CRISPY_TEMPLATE_PACK = 'bootstrap3'

############################################################
##### PROJECT-SPECIFIC #####################################
############################################################


