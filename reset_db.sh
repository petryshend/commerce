rm db.sqlite3
python3 manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'admin')" | python3 manage.py shell
sqlite3 db.sqlite3 < data.sql
