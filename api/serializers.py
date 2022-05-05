from rest_framework import serializers

from main_app.models import WitzUser, Post, Comments

class WitzUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WitzUser

        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post

        fields = "__all__"
    