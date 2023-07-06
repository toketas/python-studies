#!/bin/bash

set -e

BASE_DIR=/app/apps

run_migrations() {
  python $BASE_DIR/manage.py migrate
}

run_migrations

#exec python $BASE_DIR/manage.py runserver 0.0.0.0:8000

gunicorn -b 0.0.0.0:8000 \
    -w ${GUNICORN_WORKERS:- 1} \
    --log-level ${GUNICORN_LOG_LEVEL:- info} \
    --timeout ${GUNICORN_TIMEOUT:- 30} \
    --chdir apps \
    apps.wsgi
