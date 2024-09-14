import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from users.models import Payment
from courses.models import Course, Lesson
from users.models import User


class Command(BaseCommand):
    help = 'Загрузка платежи из файла JSON в модель платежей.'

    def handle(self, *args, **kwargs):
        # Путь к файлу payment_data.json
        fixture_path = os.path.join(settings.BASE_DIR, 'users', 'payment_data.json')

        if not os.path.exists(fixture_path):
            self.stdout.write(self.style.ERROR(f"Файл не найден: {fixture_path}"))
            return

        # Чтение файла
        try:
            with open(fixture_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR("Ошибка чтения файла JSON"))
            return

        # Проверка и загрузка данных
        for item in data:
            try:
                # Получаем данные из полей
                user_id = item['fields']['user']
                course_id = item['fields']['course']
                lesson_id = item['fields']['lesson']
                payment_date = item['fields']['payment_date']
                amount = item['fields']['amount']
                payment_method = item['fields']['payment_method']

                # Проверяем наличие пользователя
                try:
                    user = User.objects.get(pk=user_id)
                except User.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Пользователь с идентификатором {user_id} не существует."))
                    continue

                # Проверяем наличие курса (если указан)
                course = None
                if course_id:
                    try:
                        course = Course.objects.get(pk=course_id)
                    except Course.DoesNotExist:
                        self.stdout.write(self.style.ERROR(f"Курс с идентификатором {course_id} не существует."))
                        continue

                # Проверяем наличие урока (если указан)
                lesson = None
                if lesson_id:
                    try:
                        lesson = Lesson.objects.get(pk=lesson_id)
                    except Lesson.DoesNotExist:
                        self.stdout.write(self.style.ERROR(f"Урок с идентификатором {lesson_id} не существует."))
                        continue

                # Создаем запись платежа
                Payment.objects.create(
                    user=user,
                    course=course,
                    lesson=lesson,
                    payment_date=payment_date,
                    amount=amount,
                    payment_method=payment_method
                )

                self.stdout.write(self.style.SUCCESS(f"Платеж успешно загружен для пользователя {user.id}"))

            except KeyError as e:
                self.stdout.write(self.style.ERROR(f"Отсутствует поле в данных JSON: {e}"))
                continue

        self.stdout.write(self.style.SUCCESS("Загрузка платежных данных завершена!"))
