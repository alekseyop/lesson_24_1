# Generated by Django 5.1.1 on 2024-09-15 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Укажите название курса",
                        max_length=255,
                        verbose_name="Название курса",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите превью курса",
                        null=True,
                        upload_to="course_previews/",
                        verbose_name="Превью курса",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Укажите описание курса",
                        null=True,
                        verbose_name="Описание курса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Укажите название лекции",
                        max_length=255,
                        verbose_name="Название лекции",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Укажите описание лекции",
                        null=True,
                        verbose_name="Описание лекции",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите превью лекции",
                        null=True,
                        upload_to="lesson_previews/",
                        verbose_name="Превью лекции",
                    ),
                ),
                (
                    "video_url",
                    models.URLField(
                        blank=True,
                        help_text="Укажите видео",
                        null=True,
                        verbose_name="Видео",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        help_text="Выберите курс",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.course",
                        verbose_name="Курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Лекция",
                "verbose_name_plural": "Лекции",
            },
        ),
    ]
