from .utils import my_send_mail
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from .models import *
from .serializer import *
from .permissions import IsNotBanned
from drf_spectacular.utils import extend_schema


class NewsViewSet(viewsets.ModelViewSet):
    """CRUD для новостей"""
    queryset = News.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NewsDetailSerializer
        return NewsSerializer

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [permissions.AllowAny]
        elif self.action == 'retrieve':
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    @extend_schema(summary="Создание новости")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(summary="Получение списка новостей")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="Получение новости детально и списка комментариев к ней")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="Удаление новости")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(summary="Редактирование новости")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    """Контроллер для комментариев"""
    queryset = News.objects.all()
    http_method_names = ['post', 'delete']

    def get_serializer_class(self):
        if self.action == 'destroy':
            return NewsCommentSerializer
        return NewsCommentCreateSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.IsAuthenticated, IsNotBanned]
        elif self.action == 'destroy':
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    @extend_schema(summary="Создание комментария")
    def create(self, request, *args, **kwargs):
        comment = NewsCommentCreateSerializer(data=request.data, context={'request': request})
        if comment.is_valid():
            comment.save()
            if request.data['parent']:
                parent_comment = NewsComment.objects.get(pk=request.data['parent'])
                text_email = 'На ваш комментарий:\n' + parent_comment.text + '\nответил ' + parent_comment.owner.username + '\nТекст: ' + request.data['text']
                my_send_mail(text_email, [parent_comment.owner.email])
        return Response(status=201)

    @extend_schema(summary="Удаление комментария")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)