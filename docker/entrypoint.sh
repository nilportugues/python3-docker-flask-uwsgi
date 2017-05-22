#!/usr/bin/env bash

# start uswgi
uwsgi --ini /opt/uwsgi/uwsgi.ini &

# start nginx.
service nginx restart

tail -f /dev/null