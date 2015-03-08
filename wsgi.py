import os, sys
#sys.path.insert(0, '/srv/sentry')
os.environ['SENTRY_CONF'] = os.environ.get('OPENSHIFT_REPO_DIR') + 'sentry.conf.py'

from sentry.wsgi import application
