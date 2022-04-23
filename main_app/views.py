from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, WitzUser, Comments
from .forms import WitzUserForm, CreatePostForm

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView

class Homepage(ListView):
    model = Post
    template_name = "main_app/home.html"
    context_object_name = "context"
    ordering = ["-date_posted"]

class PostDetailView(DetailView):
    model = Post
    context_object_name = "context"
    template_name = "main_app/detail_post.html"
    
def profile(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "main_app/profile.html", {"context": post})

def all_comments(request):
        return render(request, "main_app/comments.html", {"context": Comments.objects.all()})


def account_creation(request):
    form = WitzUserForm()

    if request.method == "POST":
        form = WitzUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
        else:
            form = WitzUserForm()
            return render(request, "main_app/form_witzuser.html", {"form": form})
    else:
        form = WitzUserForm()
        return render(request, "main_app/form_witzuser.html", {"form": form})

    
class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = "__all__"
    template_name = "main_app/create_post.html"
    redirect_field_name = "homepage"
    login_url  = "accounts/login"

    def get_success_url(self) -> str:
        return reverse("homepage")


# class CreatePost(UpdateView):
#     model = Post
#     fields = "__all__"
#     template_name = "main_app/create_post.html"

#     def get_success_url(self) -> str:
#         return reverse("homepage")

#     def get(self, request, pk):
#         context = get_object_or_404(Post, pk=pk)
#         return context
    
#     def get_queryset(self, pk):
#         super.__init__(self, pk)
#         queryset = Post.objects.get(pk=pk)
#         return queryset

    