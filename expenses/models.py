# expenses/models.py
from django.db import models
from books.models import Book

class DistributionExpense(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} - {self.description} - {self.amount}"
