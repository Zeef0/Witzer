from django.urls import path, include
from . import views

app_name = "main_app"

urlpatterns = [
   
    path("", views.Homepage.as_view(), name="homepage"),
    path("test_home", views.test_homepage, name="search_query"),
    path("comments/<int:pk>", views.all_comments, name="all_comments"),
    path("comments/<int:pk>/new_comment", views.post_comment, name="create_comment"),
    path("successfully_logout", views.logout_page, name="logout_page"),
    path("user_creation", views.account_creation, name="account_creation"),

    path("new_post/", views.CreatePost.as_view(), name="new_post"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name='post_detail'),

    path("profile/<int:pk>", views.profile, name="profile"),
    path("update_post/<int:pk>", views.UpdatePostView.as_view(), name="update_post")
]
