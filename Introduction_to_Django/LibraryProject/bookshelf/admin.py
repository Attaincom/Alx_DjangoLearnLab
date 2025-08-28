# bookshelf/admin.py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # show these columns in the changelist
    list_display = ('title', 'author', 'publication_year')

    # right-side filters
    list_filter = ('author', 'publication_year')

    # search box (top-right)
    search_fields = ('title', 'author')

    # nice-to-haves
    ordering = ('title',)
    list_per_page = 25

# (Optional) brand the admin site
admin.site.site_header = "LibraryProject Admin"
admin.site.site_title = "LibraryProject Admin"
admin.site.index_title = "Administration"
