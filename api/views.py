from os import stat
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.contrib.auth.models import User
from main_app.models import Post, WitzUser, Comments
from .serializers import WitzUserSerializer, PostSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from api import serializers

@api_view(["GET"])
def user_api(request):
    witz = get_list_or_404(WitzUser)
    serializer = WitzUserSerializer(witz, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
# Create your views here.
class UserAPIView(APIView):

    def get(self, request):
        user = get_list_or_404(WitzUser)
        serializer = WitzUserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WitzUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostAPIView(APIView):

    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return get_object_or_404(Post, pk=pk)
        except Post.DoesNotExist as e:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        post = self.get_object(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def put(self, request, pk):
        post = self.get_object(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WitzUserDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return get_object_or_404(WitzUser, pk=pk)
        except WitzUser.DoesNotExist as e:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        witz = self.get_object(pk=pk)
        serializer = WitzUserSerializer(witz)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def put(self, request, pk):
        witz = self.get_object(pk=pk)
        serializer = WitzUserSerializer(witz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        witz = self.get_object(pk=pk)
        witz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
# @api_view(["GET", "POST"])
# def blog_api(request):
#     blog = Blog.objects.all()
#     serialized_blog = BlogSerializer(blog, many=True)
#     return Response(serialized_blog.data, status=status.HTTP_201_CREATED)