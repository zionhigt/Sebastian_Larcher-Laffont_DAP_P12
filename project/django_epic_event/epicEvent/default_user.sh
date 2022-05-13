#! /usr/bin/sh

echo "from authentication.models import User; User.objects.create_superuser(first_name='seb', last_name='larcher', username='larch', email='l@g.com', password='110690')" | python manage.py shell