from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from courses.models import Course, Lesson
from courses.validators import validate_youtube_link, YouTubeValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "title", "description", "preview", "video_url"]
        validators = [
            YouTubeValidator(field="video_url")
        ]  # Валидатор для проверки ссылки на видео


class CourseSerializer(ModelSerializer):
    lessons_count = serializers.SerializerMethodField()  # Счетчик уроков

    # Поле для вывода информации обо всех уроках
    # many=True - указываем, что мы хотим получить список уроков
    lessons = LessonSerializer(many=True, read_only=True)

    # Метод для подсчета уроков
    def get_lessons_count(self, obj):
        return obj.lessons.count()  # Подсчет количества связанных уроков

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "preview",
            "description",
            "lessons_count",
            "lessons",
        ]  # Указываем новое поле в fields
