# expenses/forms.py
from django import forms
from .models import DistributionExpense

class DistributionExpenseForm(forms.ModelForm):
    class Meta:
        model = DistributionExpense
        fields = ['book', 'description', 'amount']
