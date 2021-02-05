from .serializer import UserBanSerializer, UserListSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions


User = get_user_model()


class UserList(generics.ListAPIView):
    """Все пользователи"""
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAdminUser, ]


class UpdateBanUser(generics.UpdateAPIView):
    """Блокировка пользователя"""
    queryset = User.objects.all()
    serializer_class = UserBanSerializer
    permission_classes = [permissions.IsAdminUser, ]