from . import views
from django.urls import path, include

urlpatterns = [
    path("users/", views.UserAPIView.as_view(), name="user_api"),
    path("user/<int:pk>", views.WitzUser, name="user"),
    path('posts/', views.PostAPIView.as_view(), name="all_post"),
    path('post/<int:pk>', views.PostDetailAPIView.as_view(), name="detail_post")
    
]