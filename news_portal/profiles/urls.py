from django.urls import path
from . import views


urlpatterns = [
    path('profiles/', views.UserList.as_view()),
    path('profiles/ban/<int:pk>/', views.UpdateBanUser.as_view()),
]