
from django.shortcuts import render, redirect
from app.forms import ExpenseForm

def add_expense(request):
	if request.method == 'POST':
		form = ExpenseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('expense_success')  # Redirect to home or expense list
	else:
		form = ExpenseForm()
	return render(request, 'expense/add_expense.html', {'form': form})


def expense_success(request):
    return render(request, "expense/success.html")