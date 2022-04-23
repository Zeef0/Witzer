from django.contrib import admin
from .models import WitzUser, Post, Comments

admin.site.register(WitzUser)

admin.site.register(Post)

admin.site.register(Comments)