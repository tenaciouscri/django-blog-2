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

    # ordering = (
    #     'title', # Ascending order
    #     '-date_created', # Descending order
    # ) # Adding 'order by' for selected fields 

    def get_ordering(self, request): # Dynamic functionality for different users
        if request.user.is_superuser:
            return ("title", "-date_created")
        return ("title",)


admin.site.register(Blog, BlogAdmin)  #  Registering model to admin panel
