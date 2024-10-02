from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model

User = get_user_model()


@shared_task
def deactivate_inactive_users():
    """
    Деактивирует пользователей, не заходивших более 30 дней.
    """
    one_month_ago = timezone.now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago, is_active=True)

    # Деактивируем пользователей
    inactive_users.update(is_active=False)

    print(f"{inactive_users.count()} пользователей были деактивированы.")
