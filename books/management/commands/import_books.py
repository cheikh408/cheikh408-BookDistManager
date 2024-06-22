# books/management/commands/import_books.py
import pandas as pd
from django.core.management.base import BaseCommand
from books.models import Author, Book
from categories.models import BookCategory

class Command(BaseCommand):
    help = 'Import books from an Excel spreadsheet'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the Excel file to be imported')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        self.import_data(file_path)

    def import_data(self, file_path):
        data = pd.read_excel(file_path)

        for index, row in data.iterrows():
            author, _ = Author.objects.get_or_create(name=row['Author'])
            category, _ = BookCategory.objects.get_or_create(name=row['Category'])
            Book.objects.create(
                title=row['Title'],
                author=author,
                isbn=row['ISBN'],
                publication_date=row['Publication Date'],
                category=category,
                distribution_fee=row['Distribution Fee']
            )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
