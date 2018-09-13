#!/bin/bash

# check who owns the working directory
USER_ID=$(stat -c "%u" $PWD)

# set the python run uid to the user id we just retrieved
API_RUN_UID=${API_RUN_UID:=${USER_ID}}
API_RUN_USER=${API_RUN_USER:=saruni}
API_RUN_GROUP=${API_RUN_GROUP:=saruni}

# test to see if the user already exists
API_RUN_USER_TEST=$(grep "[a-zA-Z0-9\-\_]*:[a-zA-Z]:${API_RUN_UID}:" /etc/passwd)

# Update the user to the configured UID and group
if [ -n "${API_RUN_USER_TEST}" ]; then
    echo "Update user '$API_RUN_USER'"

    usermod -l ${API_RUN_USER} $(id -un ${API_RUN_UID})
    usermod -u $API_RUN_UID -g $API_RUN_GROUP $API_RUN_USER

# Else create the user with the configured UID and group
else
    echo "Create user '$API_RUN_USER'"

    # Create the user with the corresponding group
    mkdir /home/$API_RUN_USER
    groupadd $API_RUN_GROUP
    useradd -u $API_RUN_UID -g $API_RUN_GROUP -d /home/$API_RUN_USER $API_RUN_USER
    chown $API_RUN_USER:$API_RUN_GROUP /home/$API_RUN_USER
fi

export HOME=/home/$API_RUN_USER

echo "Switching to user '$API_RUN_USER'"
su -p - ${API_RUN_USER}
python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Prepare log files and start outputting logs to stdout
echo Creating log files
cd /var/www/riverlearn-api
mkdir logs && cd /logs
touch gunicorn.log && touch access.log

tail -n 0 -f /api/logs/*.log &

# Start Gunicorn processes
echo Starting Gunicorn...
exec python manage.py runserver 0.0.0.0:8000