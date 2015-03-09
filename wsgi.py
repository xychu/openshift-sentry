#!/usr/bin/python
import os

os.environ['SENTRY_CONF'] = os.environ.get('OPENSHIFT_REPO_DIR') + 'sentry.conf.py'

from sentry.wsgi import application
