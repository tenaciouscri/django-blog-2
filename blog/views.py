from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm
from .models import Post


def home(request):
    posts = Post.objects.all().order_by("-last_modified")

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


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/edit_post.html", {"form": form})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return render(request, "blog/delete_post.html", {"post": post})
