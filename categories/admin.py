# categories/admin.py
from django.contrib import admin
from .models import BookCategory

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
