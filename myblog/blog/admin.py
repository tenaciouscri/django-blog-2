from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "categories",
        "title_tag",
        "author",
        "created_on",
        "last_modified",
    )

    def categories(self, obj):
        return ", ".join([category.name for category in obj.category.all()])


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
