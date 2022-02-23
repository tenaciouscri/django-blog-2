from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post


def home(request):
    posts = Post.objects.all().order_by("-created_on")

    context = {
        "posts": posts,
    }
    return render(request, "home.html", context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        "post": post,
    }
    return render(request, "blog/post_detail.html", context)


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/add_post.html", {"form": form})
