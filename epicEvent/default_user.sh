#! /usr/bin/sh

count_users=`psql -d epic_event_migration_test -tc "select count(*) from authentication_user"`
echo "from authentication.models import User; User.objects.create_superuser(id=$(($count_users + 1)),first_name='seb', last_name='larcher', username='larch', email='l@g.com', password='110690')" | python manage.py shell