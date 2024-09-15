from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from users.models import User, Payment
from users.serializers import UsersSerializer, PaymentSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    # Определяем фильтры для полей
    filterset_fields = ["course", "lesson", "payment_method"]

    # Поле для сортировки
    ordering_fields = ["payment_date"]

    # По умолчанию сортировать по дате оплаты
    ordering = ["payment_date"]
