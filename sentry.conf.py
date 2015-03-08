
# This file is just Python, with a touch of Django which means you
# you can inherit and tweak settings to your hearts content.
from sentry.conf.server import *

import os


DATABASES = {
    'default': {
        # You can swap out the engine for MySQL easily by changing this value
        # to ``django.db.backends.mysql`` or to PostgreSQL with
        # ``django.db.backends.postgresql_psycopg2``

        # If you change this, you'll also need to install the appropriate python
        # package: psycopg2 (Postgres) or mysql-python
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'sentry',
        'USER': os.environ.get('OPENSHIFT_POSTGRESQL_DB_USERNAME'),
        'PASSWORD': os.environ.get('OPENSHIFT_POSTGRESQL_DB_PASSWORD'),
        'HOST': os.environ.get('OPENSHIFT_POSTGRESQL_DB_HOST'),
        'PORT': os.environ.get('OPENSHIFT_POSTGRESQL_DB_PORT')
    }
}

# You should not change this setting after your database has been created
# unless you have altered all schemas first
SENTRY_USE_BIG_INTS = True

# If you're expecting any kind of real traffic on Sentry, we highly recommend
# configuring the CACHES and Redis settings

#############
## General ##
#############

# The administrative email for this installation.
# Note: This will be reported back to getsentry.com as the point of contact. See
# the beacon documentation for more information.

# SENTRY_ADMIN_EMAIL = 'your.name@example.com'
SENTRY_ADMIN_EMAIL = ''

###########
## Redis ##
###########

# Generic Redis configuration used as defaults for various things including:
# Buffers, Quotas, TSDB
redis_host = os.environ.get('OPENSHIFT_REDIS_DB_HOST') or '127.0.0.1'
redis_port = os.environ.get('OPENSHIFT_REDIS_DB_PORT') or '6379'
redis_password = os.environ.get('OPENSHIFT_REDIS_DB_PASSWORD') or ''

SENTRY_REDIS_OPTIONS = {
    'hosts': {
        0: {
            'host': redis_host,
            'port': int(redis_port),
            'password': redis_password,
        }
    }
}

###########
## Cache ##
###########

# If you wish to use memcached, install the dependencies and adjust the config
# as shown:
#
#   pip install python-memcached
#
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': ['127.0.0.1:11211'],
#     }
# }
#
# SENTRY_CACHE = 'sentry.cache.django.DjangoCache'

SENTRY_CACHE = 'sentry.cache.redis.RedisCache'

###########
## Queue ##
###########

# See http://sentry.readthedocs.org/en/latest/queue/index.html for more
# information on configuring your queue broker and workers. Sentry relies
# on a Python framework called Celery to manage queues.

CELERY_ALWAYS_EAGER = False
BROKER_URL = 'redis://:'+redis_password+'@'+redis_host+':'+redis_port

#################
## Rate Limits ##
#################

SENTRY_RATELIMITER = 'sentry.ratelimits.redis.RedisRateLimiter'

####################
## Update Buffers ##
####################

# Buffers (combined with queueing) act as an intermediate layer between the
# database and the storage API. They will greatly improve efficiency on large
# numbers of the same events being sent to the API in a short amount of time.
# (read: if you send any kind of real data to Sentry, you should enable buffers)

SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'

############
## Quotas ##
############

# Quotas allow you to rate limit individual projects or the Sentry install as
# a whole.

SENTRY_QUOTAS = 'sentry.quotas.redis.RedisQuota'

##########
## TSDB ##
##########

# The TSDB is used for building charts as well as making things like per-rate
# alerts possible.

SENTRY_TSDB = 'sentry.tsdb.redis.RedisTSDB'

##################
## File storage ##
##################

# Any Django storage backend is compatible with Sentry. For more solutions see
# the django-storages package: https://django-storages.readthedocs.org/en/latest/

SENTRY_FILESTORE = 'django.core.files.storage.FileSystemStorage'
SENTRY_FILESTORE_OPTIONS = {
    'location': (os.environ.get('OPENSHIFT_DATA_DIR') or '/tmp/') + 'sentry-files',
}

################
## Web Server ##
################

# You MUST configure the absolute URI root for Sentry:
SENTRY_URL_PREFIX = os.environ.get('SENTRY_URL_PREFIX') or 'http://sentry.example.com'  # No trailing slash!

# If you're using a reverse proxy, you should enable the X-Forwarded-Proto
# header and uncomment the following settings
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    'limit_request_line': 0,  # required for raven-js
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},
}

#################
## Mail Server ##
#################

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.environ.get('EMAIL_HOST') or 'localhost'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD') or ''
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER') or ''
EMAIL_PORT = int(os.environ.get('EMAIL_PORT') or '25')
EMAIL_USE_TLS = (os.environ.get('EMAIL_USE_TLS') or 'False') == 'True'

# The email address to send on behalf of
SERVER_EMAIL = os.environ.get('SERVER_EMAIL') or 'root@localhost'
DEFAULT_FROM_EMAIL = SERVER_EMAIL

# If you're using mailgun for inbound mail, set your API key and configure a
# route to forward to /api/hooks/mailgun/inbound/
MAILGUN_API_KEY = ''

###########
## etc. ##
###########

# Users can only be invited
# SENTRY_FEATURES['auth:register'] = False  # used for sentry v7.4.0
SENTRY_ALLOW_REGISTRATION = False

# If this file ever becomes compromised, it's important to regenerate your SECRET_KEY
# Changing this value will result in all current sessions being invalidated
SECRET_KEY = os.environ.get('SECRET_KEY') or os.environ.get('OPENSHIFT_SECRET_TOKEN') or 'PmXIfTndRubS+6mhogzZ9wNvbF/mnUgSSBR7VmeYf9pdep5E6C5+8g=='

# http://twitter.com/apps/new
# It's important that input a callback URL, even if its useless. We have no idea why, consult Twitter.
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''

# http://developers.facebook.com/setup/
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

# http://code.google.com/apis/accounts/docs/OAuth2.html#Registering
GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''

# https://github.com/settings/applications/new
GITHUB_APP_ID = ''
GITHUB_API_SECRET = ''

# https://trello.com/1/appKey/generate
TRELLO_API_KEY = ''
TRELLO_API_SECRET = ''

# https://confluence.atlassian.com/display/BITBUCKET/OAuth+Consumers
BITBUCKET_CONSUMER_KEY = ''
BITBUCKET_CONSUMER_SECRET = ''
