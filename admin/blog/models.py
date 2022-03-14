from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=250)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100)  # Prepopulated field

    def __str__(self):
        return self.title  #  Show title instead of default name
