from django.contrib import admin

from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "date_created",
        "last_modified",
        "is_draft",
    )  # Customising the way object models get displayed

    list_filter = (
        "is_draft",
        "date_created",
    )  # Adding filter as sidebar

    # ordering = (
    #     'title', # Ascending order
    #     '-date_created', # Descending order
    # ) # Adding 'order by' for selected fields

    def get_ordering(self, request):  # Dynamic functionality for different users
        if request.user.is_superuser:
            return ("title", "-date_created")
        return ("title",)

    search_fields = ("title",)  # Adding searchable fields (case insensitive)

    prepopulated_fields = {"slug": ("title",)}  # Prepopulate field

    list_per_page = 50  # Customise no. objects per page

    def set_blogs_to_published(self, request, queryset):  # Custom action
        count = queryset.update(
            is_draft=False
        )  # Also counting how many items get published
        self.message_user(
            request, f"{count} blogs have been published!"
        )  # Send message to user about successful update

    set_blogs_to_published.short_description = (
        "Mark selected blogs as published"  # Customise custom action description
    )

    actions = ("set_blogs_to_published",)  # Adding custom action to list of actions

    date_hierarchy = "date_created"  # Add navigational elements by date

    # fields = (
    #     ("title", "slug"), # Putting two fields on same line
    #     "body",
    #     "is_draft"
    #     )  # Custom fields layout

    fieldsets = (
        (
            None,
            {
                "fields": (("title", "slug"), "body"),
            },
        ),
        (
            "Advanced options",
            {
                "fields": ("is_draft",),
                "description": "Options to configure blog creation",  # Add description
            },
        ),
    )  # Custom fieldsets w/ their own title. Cannot have both fields/fieldsets


admin.site.register(Blog, BlogAdmin)  #  Registering model to admin panel
