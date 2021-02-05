from drf_spectacular.utils import extend_schema

from .serializer import UserBanSerializer, UserListSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions


User = get_user_model()


@extend_schema(summary="Список всех пользователей")
class UserList(generics.ListAPIView):
    """Все пользователи"""
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAdminUser, ]


@extend_schema(summary="Блокировка пользователя")
class UpdateBanUser(generics.UpdateAPIView):
    """Блокировка пользователя"""
    queryset = User.objects.all()
    serializer_class = UserBanSerializer
    permission_classes = [permissions.IsAdminUser, ]