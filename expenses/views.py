# expenses/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import DistributionExpense
from .forms import DistributionExpenseForm

from django.core.paginator import Paginator

def expense_list(request):
    expenses = DistributionExpense.objects.all()
    paginator = Paginator(expenses, 10)  # 10 dépenses par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'expenses/expense_list.html', {'page_obj': page_obj})


def expense_create(request):
    if request.method == 'POST':
        form = DistributionExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = DistributionExpenseForm()
    return render(request, 'expenses/expense_form.html', {'form': form})

def expense_update(request, pk):
    expense = get_object_or_404(DistributionExpense, pk=pk)
    if request.method == 'POST':
        form = DistributionExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = DistributionExpenseForm(instance=expense)
    return render(request, 'expenses/expense_form.html', {'form': form})

def expense_delete(request, pk):
    expense = get_object_or_404(DistributionExpense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})
