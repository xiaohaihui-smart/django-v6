pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
celery -A host_manager worker -l info
celery -A host_manager beat -l info
