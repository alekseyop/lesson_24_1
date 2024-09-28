# Generated by Django 5.1.1 on 2024-09-30 21:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0005_alter_course_owner"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="payment",
            options={"verbose_name": "Платеж", "verbose_name_plural": "Платежи"},
        ),
        migrations.AddField(
            model_name="payment",
            name="link",
            field=models.URLField(
                blank=True,
                help_text="Укажите ссылку на оплату",
                max_length=400,
                null=True,
                verbose_name="Ссылка на оплату",
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="session_id",
            field=models.CharField(
                blank=True,
                help_text="Укажите ID сессии",
                max_length=255,
                null=True,
                verbose_name="ID сессии",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="amount",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Сумма оплаты"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="courses.course",
                verbose_name="Оплаченный курс",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="lesson",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="courses.lesson",
                verbose_name="Оплаченный урок",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_date",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты"),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_method",
            field=models.CharField(
                choices=[("cash", "Наличные"), ("bank_transfer", "Перевод на счет")],
                max_length=20,
                verbose_name="Способ оплаты",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
    ]
