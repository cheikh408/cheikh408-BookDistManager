# reports/views.py
from django.shortcuts import render
from categories.models import BookCategory
from books.models import Book
from django.db.models import Sum

def expense_report(request):
    categories = BookCategory.objects.all()
    report_data = []

    for category in categories:
        total_expense = Book.objects.filter(category=category).aggregate(total=Sum('distribution_fee'))['total'] or 0
        report_data.append({'category': category.name, 'total_expense': total_expense})

    return render(request, 'reports/expense_report.html', {'report_data': report_data})
