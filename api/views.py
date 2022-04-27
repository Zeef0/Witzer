from django.shortcuts import render


def post_api(request):
    return render(request, "main_app/home.html")
# Create your views here.
