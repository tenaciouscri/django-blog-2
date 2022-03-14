from django.contrib import admin
from django.utils import timezone
from django.db.models import Count

from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from django_summernote.admin import SummernoteModelAdmin

from blog.models import Blog, Comment, Category


class CommentInline(admin.TabularInline):  # Showing comments in blog admin page
    # Could also be StackedInline
    model = Comment
    fields = ("text", "is_active")
    extra = 1  # By default 3 empty boxes at the end
    classes = ("collapse",)


class BlogAdmin(SummernoteModelAdmin):

    list_display = (
        "title",
        "date_created",
        "last_modified",
        "is_draft",
        "days_since_creation",
        "no_of_comments",
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
                "fields": ("is_draft", "categories", ),
                "description": "Options to configure blog creation",  # Add description
                "classes": ("collapse",),  # Make section collapsible
            },
        ),
    )  # Custom fieldsets w/ their own title. Cannot have both fields/fieldsets

    # This function could also be added to models.py
    def days_since_creation(self, blog):  # Returning no. of days since creation
        diff = timezone.now() - blog.date_created
        return diff.days

    days_since_creation.short_description = "Days active"

    # Apply Summernote to all TextField in model
    summernote_fields = ("body",)

    inlines = (CommentInline,)  # Adding inlines at the end of the page

    def get_queryset(self, request):
        """
        Overriding changelist queries
        """
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(comments_count=Count("comments"))
        return queryset

    def no_of_comments(self, blog):
        return blog.comments_count

    no_of_comments.admin_order_field = "comments_count"

    filter_horizontal = ("categories", ) # Make many-to-many field more user friendly


class CommentAdmin(admin.ModelAdmin):

    list_display = ("blog", "text", "date_created", "is_active")
    list_editable = ("is_active",)  # Editable in table
    list_per_page = 20
    list_filter = (
        ("blog", RelatedDropdownFilter),
    )


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)  #  Registering model to admin panel
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
