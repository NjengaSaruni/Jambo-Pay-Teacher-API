#!/usr/bin/env bash

# wait for PSQL server to start
sleep 10

# migrate db, so we have the latest db schema
su -m workforce_user -c "python manage.py migrate"

# start development server on public ip interface, on port 8000
su -m workforce_user -c "python manage.py collectstatic"

# start development server on public ip interface, on port 8000
su -m workforce_user -c "python manage.py runserver 0.0.0.0:8000"