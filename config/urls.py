from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "", include("courses.urls")
    ),  # Подключаем отдельные маршруты для курсов.urls")),  # Подключаем отдельные маршруты для уроков
    path("", include("users.urls")),  # Подключаем отдельные маршруты для пользователей
]
