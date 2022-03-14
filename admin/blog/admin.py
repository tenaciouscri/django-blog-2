from django.contrib import admin

from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "date_created",
        "last_modified",
        "is_draft",
    )  # Customising the way object models get displayed

    list_filter = ("is_draft",)  # Adding filter as sidebar


admin.site.register(Blog, BlogAdmin)  #  Registering model to admin panel
