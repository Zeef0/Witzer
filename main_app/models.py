from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone

from django.db.models import CharField
from django.db.models.functions import Lower, Length
from typing import Optional,Iterable
CharField.register_lookup(Length)


class WitzUser(models.Model):
    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
        ("Other", "Other"),
        (None, "Select one only"),


    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, default=" ", choices=GENDER)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    # def save(self, **kwargs):
    #     some_salt = 'some_salt' 
    #     password = make_password(self.password1, some_salt)
    #     if not self.id:
    #         raise ValidationError("You must have to provide routing for multiple services deployment.")
    #     super().save(**kwargs)

class Comments(models.Model):
    
    witzer = models.ForeignKey(User, models.CASCADE)
    content = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "comments"
        

    def __str__(self) -> str:
        return self.content

class Post(models.Model):
    author = models.ForeignKey(WitzUser, on_delete=models.CASCADE)
    post = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    post_count_like = models.IntegerField(default=0)
    
    class Meta:
        ordering = ["date_posted"]

    def __str__(self):
     return self.post
