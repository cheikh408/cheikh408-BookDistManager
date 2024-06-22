# books/models.py
from django.db import models
from categories.models import BookCategory

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField()
    category = models.ForeignKey(BookCategory, on_delete=models.SET_NULL, null=True)
    distribution_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
