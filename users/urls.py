from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    UsersViewSet,
    RegisterView,
    PaymentCreateAPIView,
    PaymentSuccessAPIView,
    PaymentCancelAPIView,
    PaymentStatusAPIView,
)  # Импортируем ViewSet для пользователей


app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"users", UsersViewSet)  # Регистрируем ViewSet для пользователей

urlpatterns = [
    path("", include(router.urls)),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Подключаем маршруты API для курсов и пользователей
    path("api/register/", RegisterView.as_view(), name="register"),
    path("payments/", PaymentCreateAPIView.as_view(), name="payment_create"),  # Оплата
    path(
        "payment-success/", PaymentSuccessAPIView.as_view(), name="payment_success"
    ),  # Ссылка на оплату
    path(
        "payment-cancel/", PaymentCancelAPIView.as_view(), name="payment_cancel"
    ),  # Отмена платежа
    path(
        "payment-status/<str:session_id>/",
        PaymentStatusAPIView.as_view(),
        name="payment_status",
    ),
]
