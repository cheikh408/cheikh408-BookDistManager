# reports/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('expenses/', views.expense_report, name='expense_report'),
]
