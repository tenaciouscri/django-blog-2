from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path(
        "post/category/<str:category>/",
        views.posts_by_category,
        name="post_by_category",
    ),
    path("post/add_post/", views.add_post, name="add_post"),
    path("post/add_category/", views.add_category, name="add_category"),
    path("post/edit_post/<int:pk>/", views.edit_post, name="edit_post"),
    path("post/delete_post/<int:pk>/", views.delete_post, name="delete_post"),
]
