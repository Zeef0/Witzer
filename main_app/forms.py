from email.policy import default
from logging import PlaceHolder
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Post, WitzUser, Comments


class WitzUserForm(UserCreationForm):
    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
        ("Other", "Other")
    )
    
    gender = forms.ChoiceField(choices=GENDER)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


        widgets = {
            "content": forms.TextInput(attrs={"class": "form-control"})
        }

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comments 
        fields = ["content"]
        