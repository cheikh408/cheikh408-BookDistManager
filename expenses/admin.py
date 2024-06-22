# expenses/admin.py
from django.contrib import admin
from .models import DistributionExpense

@admin.register(DistributionExpense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('book', 'description', 'amount', 'date')
    search_fields = ('book__title', 'description')
    list_filter = ('book', 'date')
    date_hierarchy = 'date'
