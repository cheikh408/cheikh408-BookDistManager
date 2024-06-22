# categories/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import BookCategory
from .forms import BookCategoryForm
from django.core.paginator import Paginator

def category_list(request):
    categories = BookCategory.objects.all()
    paginator = Paginator(categories, 10)  # Show 10 categories per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'categories/category_list.html', {'page_obj': page_obj})

def category_create(request):
    if request.method == 'POST':
        form = BookCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = BookCategoryForm()
    return render(request, 'categories/category_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(BookCategory, pk=pk)
    if request.method == 'POST':
        form = BookCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = BookCategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(BookCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'categories/category_confirm_delete.html', {'category': category})
