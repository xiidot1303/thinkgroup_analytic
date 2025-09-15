from django.contrib import admin
from app.models import Branch, Category, Expense
from rangefilter.filters import DateRangeFilter
from app.forms import ExpenseForm
from unfold.admin import ModelAdmin as UnfoldModelAdmin


@admin.register(Branch)
class BranchAdmin(UnfoldModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address') 

@admin.register(Category)
class CategoryAdmin(UnfoldModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Expense)
class ExpenseAdmin(UnfoldModelAdmin):
    # form 
    list_display = ('branch', 'category', 'amount', 'staff', 'date')
    list_filter = ('branch', 'category', ("date", DateRangeFilter))
    search_fields = ('branch__name', 'category__name', 'description')

    autocomplete_fields = ["branch", "category"]