#! /usr/bin/sh

psql -d postgres < restore_epic_event.sql &&
./manage.py migrate admin &&
./manage.py migrate auth &&
./manage.py migrate customer &&
./manage.py migrate event &&
./manage.py migrate contrat &&
./manage.py migrate authentication &&
./manage.py migrate &&
./default_user.sh &&
./manage.py runserver
