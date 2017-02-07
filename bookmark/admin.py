from django.contrib import admin
from bookmark.models import Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['link', 'title', 'tag_list']

    def get_queryset(self, request):
        return super(BookmarkAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u', '.join(o.name for o in obj.tags.all())

admin.site.register(Bookmark, BookmarkAdmin)

# Register your models here.
