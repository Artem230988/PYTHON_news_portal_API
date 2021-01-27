# class NewsCommentCreateView(generics.CreateAPIView):
#     """Создание комментария"""
#     serializer_class = NewsCommentCreateSerializer
#     permission_classes = [permissions.IsAuthenticated, IsNotBanned]
#
#     @extend_schema(summary="Создание комментария")
#     def post(self, request, *args, **kwargs):
#         comment = NewsCommentCreateSerializer(data=request.data, context={'request': request})
#         if comment.is_valid():
#             comment.save()
#             if request.data['parent']:
#                 parent_comment = NewsComment.objects.get(pk=request.data['parent'])
#                 text_email = 'На ваш комментарий:\n' + parent_comment.text + '\nответил ' + parent_comment.owner.username + '\nТекст: ' + request.data['text']
#                 send_mail('News_portal info', text_email, settings.EMAIL_HOST_USER, [parent_comment.owner.email], fail_silently=False)
#         return Response(status=201)

#
# class NewsCommentDeleteView(generics.DestroyAPIView):
#     """Удаление комментария"""
#     queryset = NewsComment.objects.all()
#     serializer_class = NewsCommentSerializer
#     permission_classes = [permissions.IsAdminUser]
#
#     @extend_schema(summary="Удаление комментария")
#     def destroy(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)


#     [
#     # path('news/', views.NewsListView.as_view()),
#     # path('news/<int:pk>/', views.NewsDetailView.as_view()),
#     # path('news/<int:pk>/update', views.NewsUpdateView.as_view()),
#     # path('news/<int:pk>/delete', views.NewsDeleteView.as_view()),
#     # path('news/create', views.NewsCreateView.as_view()),
#
#     path('comment_create', views.NewsCommentCreateView.as_view()),
#     path('comment_delete/<int:pk>', views.NewsCommentDeleteView.as_view()),
#
# ]