from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

from courses.models import Course, Lesson

NULLABLE = {"null": True, "blank": True}  # Необязательное поле


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Адрес электронной почты"
    )
    phone = models.CharField(
        max_length=35,
        **NULLABLE,
        verbose_name="Телефон",
        help_text="Укажите номер телефона",
    )
    city = models.CharField(
        max_length=100, **NULLABLE, verbose_name="Город", help_text="Укажите ваш город"
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        **NULLABLE,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:  # Метаданные
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    """
    Модель платежа, которая хранит информацию о платежах, связанных с курсами и уроками.

    Поля:
    - user: Пользователь, совершивший платеж.
    - payment_date: Дата и время, когда был совершен платеж.
    - course: Курс, за который был осуществлен платеж.
    - lesson: Урок, за который был осуществлен платеж.
    - amount: Сумма платежа.
    - payment_method: Способ оплаты (наличные или перевод на счет).

    Методы:
    - __str__: Возвращает строковое представление платежа в формате: "email пользователя - сумма (способ оплаты)".
    """

    CASH = "cash"
    BANK_TRANSFER = "bank_transfer"

    PAYMENT_METHOD_CHOICES = [
        (CASH, "Наличные"),
        (BANK_TRANSFER, "Перевод на счет"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты")
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Оплаченный курс",
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Оплаченный урок",
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Сумма оплаты"
    )
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD_CHOICES, verbose_name="Способ оплаты"
    )
    session_id = models.CharField(
        max_length=255,
        **NULLABLE,
        verbose_name="ID сессии",
        help_text="Укажите ID сессии",
    )
    link = models.URLField(
        max_length=400,
        **NULLABLE,
        verbose_name="Ссылка на оплату",
        help_text="Укажите ссылку на оплату",
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        """
        Возвращает строковое представление платежа в формате:
        'email пользователя - сумма (способ оплаты) '.
        """
        return (
            f"{self.user.email} - {self.amount} ({self.get_payment_method_display()})"
        )
