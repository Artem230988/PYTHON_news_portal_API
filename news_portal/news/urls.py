from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()
router.register(r'news', views.NewsViewSet, basename='news')

router2 = SimpleRouter()
router2.register(r'comment', views.CommentViewSet, basename='comment')

urlpatterns = router.urls + router2.urls
