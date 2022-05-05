from email.policy import default
from logging import PlaceHolder
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _
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
        fields = ["post", "pictures"]
        
        labels = {
            'post': _('Write a post'),
            'pictures': _("Upload a picture"),
        }

        # widgets = {
        #     'pictures': forms.TextInput(attrs={'class': 'btn-success'}),
        # }       


        # def __init__(self, *args, **kwargs):
        #     super(CreatePostForm, self).__init__(*args, **kwargs)
        #     self.fields['pictures'].widget.attrs.update({'class': 'btn btn-success'})
class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comments 
        fields = ["content"]
        