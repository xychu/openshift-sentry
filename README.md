Sentry Quickstart For OpenShift
===============================

This repository is set up to install Sentry onto an OpenShift server.  It is currently configured
to install as an un-scaled single gear component, but should be easily able to be converted to use
PostgreSQL and scale.

To install:

    rhc create-app sentry python-2.7 \
        http://cartreflect-claytondev.rhcloud.com/reflect?github=gerardogc2378/openshift-redis-cart \
        --from-code=https://github.com/smarterclayton/sentry \
        SENTRY_URL_PREFIX="https://sentry-<yourdomain>.rhcloud.com"

The login credentials are "admin"/"admin" by default - please change them after installation. User
self registration is disabled as well, so only invites can add people to your application.

See `default.conf` for other enviroment variables that can be set.
