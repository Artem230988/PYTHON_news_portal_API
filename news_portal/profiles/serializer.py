from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserBanSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        queryset = model.objects.all()
        fields = ('is_banned', )


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        queryset = model.objects.all()
        fields = ('id', 'username', 'email', 'is_banned', 'is_active', 'is_staff')