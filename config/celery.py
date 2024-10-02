import os
from celery import Celery

# Указываем Django настройки как настройки для Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

# Загружаем настройки Celery из переменных окружения
app.config_from_object("django.conf:settings", namespace="CELERY")

# Автоматическое нахождение задач (tasks) в приложениях
app.autodiscover_tasks()
