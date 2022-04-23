from django.urls import path, include
from . import views

app_name = "main_app"

urlpatterns = [
   
    path("", views.Homepage.as_view(), name="homepage"),
    path("comments/", views.all_comments, name="all_comments"),
    path("user_creation", views.account_creation, name="account_creation"),

    path("new_post/", views.CreatePost.as_view(), name="new_post"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name='post_detail'),

    path("profile/<int:pk>", views.profile, name="profile"),
    path("update_post/<int:pk>", views.UpdatePostView.as_view(), name="update_post")
]
