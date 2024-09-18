from .apps import CoursesConfig
from .views import LessonListCreateView, LessonRetrieveUpdateDestroyView, LessonViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses.views import CourseViewSet

app_name = CoursesConfig.name

router = DefaultRouter()
router.register(r"courses", CourseViewSet)  # Регистрируем ViewSet для курсов
router.register(r"lessons", LessonViewSet)  # Регистрируем ViewSet для лекций

urlpatterns = [
    path("lessons/", LessonListCreateView.as_view(), name="lesson-list-create"),
    path(
        "lessons/<int:pk>/",
        LessonRetrieveUpdateDestroyView.as_view(),
        name="lesson-detail",
    ),
    path(
        "", include(router.urls)
    ),  # Подключаем маршруты API для курсов и пользователей
]
