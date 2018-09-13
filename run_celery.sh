#!/usr/bin/env bash

# wait for RabbitMQ server to start
sleep 1

# copy local settings into a celery settings model
cp ./config/local_settings.py    ./config/celery_settings.py
#running celery in deve environment
su -m workforce_user -c "celery -A api worker -B --loglevel=INFO"  
