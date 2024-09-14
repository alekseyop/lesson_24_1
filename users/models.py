from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}  # Необязательное поле


class User(AbstractUser):

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Адрес электронной почты"
    )
    phone = models.CharField(
        max_length=35,
        **NULLABLE,
        verbose_name="Телефон",
        help_text="Укажите номер телефона"
    )
    city = models.CharField(
        max_length=100, **NULLABLE, verbose_name="Город", help_text="Укажите ваш город"
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        **NULLABLE,
        verbose_name="Аватар",
        help_text="Загрузите аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']  # Поля, обязательные для заполнения при создании пользователя

    def __str__(self):
        return self.email

    class Meta:  # Метаданные
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
