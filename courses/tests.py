import unittest
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from users.models import User
from .models import Course, Lesson, CourseSubscription



class CourseTestCase(APITestCase):
#  class CourseLessonTests(unittest.TestCase):
    def setUp(self):
        # Создаем тестового пользователя и курс с уроком
        self.client = APIClient()

        self.user = User.objects.create(email="testuser1@example.com", password="password123")
        self.user.set_password("password123")
        self.user.save()

        self.course = Course.objects.create(title='Test Course', description='Course description', owner=self.user)
        self.lesson = Lesson.objects.create(title='Test Lesson', description='Lesson description', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)  # Авторизуемся

    def test_create_lesson(self):
        # Аутентифицируем пользователя

        self.client.force_authenticate(user=self.user)
        data = {'title': 'New Lesson', 'description': 'New lesson description', 'course': self.course.id}
        response = self.client.post(reverse('courses:lesson-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_lesson(self):
        # Проверяем получение урока
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('courses:lesson-detail', kwargs={'pk': self.lesson.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lesson(self):
        # Обновление урока
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Updated Lesson', 'description': 'Updated lesson description'}
        response = self.client.put(reverse('courses:lesson-detail', kwargs={'pk': self.lesson.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lesson(self):
        # Удаление урока
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse('courses:lesson-detail', kwargs={'pk': self.lesson.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


#  class CourseTestCase(APITestCase):
class CourseSubscriptionTests(APITestCase):
#  class CourseSubscriptionTests(unittest.TestCase):
    def setUp(self):
        # Создаем тестового пользователя и курс
        self.client = APIClient()
        self.user = User.objects.create(email="testuser1@example.com", password="password123")

        self.course = Course.objects.create(title='Test Course', description='Course description', owner=self.user)

    def test_subscribe_course(self):
        # Подписка на курс
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('courses:course-subscribe', kwargs={'course_id': self.course.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(CourseSubscription.objects.filter(user=self.user, course=self.course).exists())

    def test_unsubscribe_course(self):
        # Отписка от курса
        CourseSubscription.objects.create(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('courses:course-subscribe', kwargs={'course_id': self.course.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(CourseSubscription.objects.filter(user=self.user, course=self.course).exists())
