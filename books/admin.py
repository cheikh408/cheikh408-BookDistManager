# books/admin.py
from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'publication_date', 'isbn', 'distribution_fee')
    search_fields = ('title', 'author__name', 'category__name', 'isbn')
    list_filter = ('category', 'author')
    date_hierarchy = 'publication_date'
