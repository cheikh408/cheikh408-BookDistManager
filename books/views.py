# books/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.core.files.storage import FileSystemStorage
import pandas as pd
from django.core.paginator import Paginator

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)  # Show 10 books per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'books/book_list.html', {'page_obj': page_obj})
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})




def import_excel(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        # Validation du type de fichier (optionnel)
        if not excel_file.name.endswith('.xls') and not excel_file.name.endswith('.xlsx'):
            return render(request, 'import_excel.html', {'error_message': 'Only Excel files are allowed.'})

        # Lecture du fichier Excel
        df = pd.read_excel(excel_file)
        # Traitement du dataframe df comme requis
        
        return render(request, 'import_excel.html', {'success_message': 'File uploaded successfully.'})
    
    return render(request, 'import_excel.html')
