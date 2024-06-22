# rumipress/views.py
# views.py

from django.shortcuts import render
import pandas as pd

from books.models import Author, Book
from categories.models import BookCategory

def home(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        # Validation du type de fichier (optionnel)
        if not excel_file.name.endswith('.xls') and not excel_file.name.endswith('.xlsx'):
            return render(request, 'home.html', {'error_message': 'Only Excel files are allowed.'})

        # Lecture du fichier Excel
        df = pd.read_excel(excel_file)
        # Traitement du dataframe df comme requis
        # Par exemple, vous pouvez créer des objets de modèle à partir des données
        for index, row in df.iterrows():
            # Supposez que vous ayez un modèle Book avec les champs correspondants
            # Author doit être créé ou récupéré en fonction de votre logique
            author, created = Author.objects.get_or_create(name=row['Author'])
            category, created = BookCategory.objects.get_or_create(name=row['Category'])
            Book.objects.create(
                title=row['Title'],
                author=author,
                isbn=row['ISBN'],
                publication_date=row['Publication Date'],
                category=category,
                distribution_fee=row['Distribution Fee']
            )

        return render(request, 'home.html', {'success_message': 'File uploaded and processed successfully.'})
    
    return render(request, 'home.html')
