from .common import *

DEBUG = True
# Testing
INSTALLED_APPS += ('django_nose', 'django_extensions', 'corsheaders')
MIDDLEWARE = ('corsheaders.middleware.CorsMiddleware', ) + MIDDLEWARE

CORS_ORIGIN_WHITELIST = (os.getenv('CLIENT_URL', 'localhost:8080'), )
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = bool(strtobool(os.getenv('CORS_ORIGIN_ALLOW_ALL', 'False')))

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [BASE_DIR, '-s', '--nologcapture', '--with-coverage', '--with-progressive', '--cover-package=bgdb']

# Mail
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
NOTEBOOK_ARGUMENTS = ['--ip', '0.0.0.0', '--no-browser', '--allow-root']
