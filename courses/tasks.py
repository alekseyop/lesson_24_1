from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_course_update_email(user_email, course_title):
    """
    Асинхронная задача для отправки письма об обновлении курса.
    """
    subject = f"Обновление курса: {course_title}"
    message = f"Курс '{course_title}' был обновлен. Проверьте новые материалы!"
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, email_from, recipient_list)
