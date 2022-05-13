#! /usr/bin/bash

set -e
psql -d postgres < restore_epic_event.sql
# ./manage.py migrate admin
# ./manage.py migrate customer
# ./manage.py migrate event
./manage.py migrate contrat
./manage.py migrate
./default_user.sh
./manage.py runserver
