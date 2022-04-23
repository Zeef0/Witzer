from django.urls import path, include
from . import views
urlpatterns = [
   
    path("", views.Homepage.as_view(), name="homepage"),
    path("comments/", views.all_comments, name="all_comments"),
    path("user_creation", views.account_creation, name="account_creation"),
    path("new_post/", views.CreatePost.as_view(), name="new_post"),
    # path("update_post/<int:pk>", views.UpdateView.as_view(), name="update_post")
]
