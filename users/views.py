from rest_framework import viewsets

from users.models import User
from users.serializers import UsersSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
