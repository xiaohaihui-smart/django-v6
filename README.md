# 使用的python环境3.10

pip install -r requirements.txt

# 启动数据库迁移
python manage.py migrate


# 启动程序
python manage.py runserver


# 初始化定时任务
celery -A host_manager worker -l info


# 启动定时任务
celery -A host_manager beat -l info
