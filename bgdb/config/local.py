from .common import *

DEBUG = True
# Testing
INSTALLED_APPS += ('django_nose', 'django_extensions')
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    BASE_DIR,
    '-s',
    '--nologcapture',
    '--with-coverage',
    '--with-progressive',
    '--cover-package=bgdb'
]

# Mail
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
NOTEBOOK_ARGUMENTS = ['--ip', '0.0.0.0', '--no-browser', '--allow-root']
