from django.contrib import admin
from .models import Book


# Register your models here.

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'language', 'status')
    list_filter = ('genre', 'status', 'year', 'language')
    search_fields = ('title', 'author')
    ordering = ('title', 'year')
