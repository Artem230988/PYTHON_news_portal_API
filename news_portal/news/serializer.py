from rest_framework import serializers

from .models import *


class FilterNewsCommentSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializer = NewsCommentSerializer(value, context=self.context)
        # serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class NewsSerializer(serializers.ModelSerializer):
    """Список новостей"""
    class Meta:
        model = News
        fields = '__all__'


class NewsCommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментария к новости"""
    username = serializers.CharField(source='owner.username')
    children = RecursiveSerializer(many=True, allow_null=True)

    def get_level(self, obj):
        return obj.level

    def validate(self, attrs):
        instance = NewsComment(**attrs)
        instance.clean()
        return attrs

    class Meta:
        list_serializer_class = FilterNewsCommentSerializer
        model = NewsComment
        fields = ('id', 'username', 'text', 'created_at', 'level', 'children')


class NewsDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для новости"""
    comments = NewsCommentSerializer(many=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'created_at', 'comments')


class NewsCommentCreateSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        instance.owner = self.context['request'].user
        instance.save()
        return instance

    class Meta:
        model = NewsComment
        fields = ('text', 'news', 'parent',)
