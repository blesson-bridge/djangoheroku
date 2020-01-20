import os
from .common import Common
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Common):
    DEBUG = True

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ('django_nose','rest_framework_swagger')
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        BASE_DIR,
        '-s',
        '--nologcapture',
        '--with-coverage',
        '--with-progressive',
        '--cover-package=companies'
    ]

    # Mail
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    SECRET_KEY = 'y2cr-u&m7$x2$=#*a0s&&lavd^4=9arcy8h_%ktxohm+1ea!6d'
    REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'companies_data',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

