Sentry For OpenShift
====================

This repository is set up to install Sentry onto an OpenShift server.

It is currently configured to install as a scaled component using PostgreSQL and Redis.

To install:

    rhc app create sentry python-2.7 postgresql-9.2 \
        http://cartreflect-claytondev.rhcloud.com/reflect?github=gerardogc2378/openshift-redis-cart \
        --from-code=https://github.com/xychu/openshift-sentry \
        SENTRY_URL_PREFIX="https://sentry-<yourdomain>.rhcloud.com" -s

The login credentials are "admin"/"admin" by default - please change them after installation. User
self registration is disabled as well, so only invites can add people to your application.

See `sentry.conf.py` for other enviroment variables that can be set.
