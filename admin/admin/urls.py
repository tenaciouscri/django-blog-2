from django.contrib import admin
from django.urls import path

admin.site.site_header = 'The Admin Lair' #  Change header of admin panel
admin.site.site_title = 'The Admin Lair' #  Change title of admin panel
admin.site.index_title = 'The Admin Lair administration' # Customise 'Site administration'

urlpatterns = [
    path('admin/', admin.site.urls),
]
