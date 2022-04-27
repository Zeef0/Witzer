from . import views
from django.urls import path, include

urlpatterns = [
    path("posts/ ", views.post_api, name="post_api")
]