from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from members.forms import CustomUserCreationForm


def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html", {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            return redirect(reverse("home"))
