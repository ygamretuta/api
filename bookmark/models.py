from __future__ import unicode_literals

from django.db import models
from taggit.managers import TaggableManager


class Bookmark(models.Model):
    link = models.URLField()
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
