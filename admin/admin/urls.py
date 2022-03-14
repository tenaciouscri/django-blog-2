from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings  # Summernote

admin.site.site_header = "The Admin Lair"  #  Change header of admin panel
admin.site.site_title = "The Admin Lair"  #  Change title of admin panel
admin.site.index_title = (
    "The Admin Lair administration"  # Customise 'Site administration'
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )  # Summernote
