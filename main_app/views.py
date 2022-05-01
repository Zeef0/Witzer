from django.urls import reverse
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from .models import Post, WitzUser, Comments
from .forms import WitzUserForm, CreatePostForm, PostCommentForm

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

class Homepage(ListView):
    model = Post
    template_name = "main_app/home.html"
    context_object_name = "context"
    ordering = ["-date_posted"]

class PostDetailView(DetailView):
    model = Post
    context_object_name = "context"
    template_name = "main_app/detail_post.html"
    
    


class UpdatePostView(UpdateView):
    model = Post
    fields = ["post"]
    template_name = "main_app/create_post.html"

    

    # def get_success_url(self) -> str:
    #     return reverse("homepage")

    # def get(self, request, pk):
    #     context = get_object_or_404(Post, pk=pk)
    #     return context
    
    # def get_queryset(self, pk):
    #     super.__init__(self, pk)
    #     queryset = Post.objects.get(pk=pk)
    #     return 
    
class PostDeleteView(DeleteView):
    model = Post
    context_object_name = "context"
    
    success_url = "/"
    
    
class CreatePost(LoginRequiredMixin, CreateView):
    
    model = Post
    template_name = "main_app/create_post.html"
    redirect_field_name = "homepage"
    login_url  = "accounts/login"
    form_class = CreatePostForm
    
    def get_success_url(self) -> str:
        return reverse("homepage")

@login_required
def create_post(request):
    form = CreatePostForm()
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect("main_app:homepage")
    return render(request, "main_app/create_comment.html", {"form": form})

def test_homepage(request, pk):
    post = get_object_or_404(Post, pk=pk)

    print(post.author, request.user)
    print(str(post.author) == str(request.user))
    print(type(request.user), type(post.author)) # SMH


    return render(request, "main_app/test.html", {"context": post})

def profile(request, pk):
    post = get_object_or_404(WitzUser, pk=pk)
    # test = Post.objects.all().filter(author=pk)
    return render(request, "main_app/profile.html", {"context": post})

def all_comments(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, "main_app/comments.html", {"context": post})

@login_required
def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostCommentForm()
    if request.method == "POST":
        form = PostCommentForm(request.POST)
        if form.is_valid():
            form.instance.post = post
            form.instance.witzer = request.user
            form.save()
            return redirect("main_app:homepage")
    return render(request, "main_app/create_comment.html", {"context": post, "form": form})

def account_creation(request):
    form = WitzUserForm()

    if request.method == "POST":
        form = WitzUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
        else:
            form = WitzUserForm()
            print(form)
            return render(request, "main_app/form_witzuser.html", {"form": form})
    else:
        form = WitzUserForm()
        return render(request, "main_app/form_witzuser.html", {"form": form})


def logout_page(request):
    return render(request, "main_app/magma.html")


@login_required
def add_like(request, pk):
    post = get_object_or_404(Post, pk=pk)

    print(f"Post before increment {post.post_count_like}")
    post.post_count_like += 1
    print(f"Post before increment {post.post_count_like}")
    post.save()
    return redirect("main_app:homepage")