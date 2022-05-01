from django.urls import path, include
from . import views

app_name = "main_app"

urlpatterns = [
   
    path("", views.Homepage.as_view(), name="homepage"),
    path("test_home/<int:pk>", views.test_homepage, name="search_query"),
    path("comments/<int:pk>", views.all_comments, name="all_comments"),
    path("comments/<int:pk>/new_comment", views.post_comment, name="create_comment"),


    path("profile/<int:pk>", views.profile, name="profile"),
    path("user_creation", views.account_creation, name="account_creation"),
    path("successfully_logout", views.logout_page, name="logout_page"),

    path("post/<int:pk>", views.PostDetailView.as_view(), name='post_detail'),
    path("like/post/<int:pk>", views.add_like, name='like_post'),
    path("new_post/", views.create_post, name="new_post"),
    path("update/post/<int:pk>", views.UpdatePostView.as_view(), name="update_post"),
    path("delete/post/<int:pk>", views.PostDeleteView.as_view(), name="delete_post"),
]
