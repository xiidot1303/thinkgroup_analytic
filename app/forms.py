from django.forms import ModelForm
from app.models import *
from django import forms
from unfold.forms import AdminForm


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["branch", "category", "amount", "description", "date", "staff"]

        widgets = {
            "branch": forms.Select(attrs={"class": "form-select"}),
            "category": forms.Select(attrs={"class": "form-select category-select"}),
            "amount": forms.NumberInput(attrs={"class": "form-control", "placeholder": "100000"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Qo‘shimcha ma’lumot..."}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date", "required": False}),
            "staff": forms.Select(attrs={"class": "form-select"}),
        }

        labels = {
            "branch": "Filial",
            "category": "Kategoriya",
            "staff": "",
            "amount": "Miqdor",
            "description": "Izoh",
            "date": "Sana",
        }