#!/usr/bin/env bash

source /opt/market-force-api/bin/activate
exec gunicorn  --timeout=60 --graceful-timeout=30 --bind 127.0.0.1:8000 config.wsgi
