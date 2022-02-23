from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "title_tag",
        "author",
        "created_on",
        "last_modified",
    )


admin.site.register(Post, PostAdmin)
