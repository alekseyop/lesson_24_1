from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from courses.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    lessons_count = serializers.SerializerMethodField()  # Счетчик уроков

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
    ]  # Указываем новое поле в fields


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "title", "description", "preview", "video_url", "course"]
