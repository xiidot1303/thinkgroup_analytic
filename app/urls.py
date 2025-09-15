from django.urls import path, re_path
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordChangeDoneView, 
    PasswordChangeView
)

from app.views import (
    main
)
from app.views.expense import add_expense, expense_success

urlpatterns = [
    path('', main.main),
    # login
    path('accounts/login/', LoginView.as_view()),
    path('changepassword/', PasswordChangeView.as_view(
        template_name = 'registration/change_password.html'), name='editpassword'),
    path('changepassword/done/', PasswordChangeDoneView.as_view(
        template_name = 'registration/afterchanging.html'), name='password_change_done'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # files
    re_path(r'^files/(?P<path>.*)$', main.get_file),

    # add expense (mobile)
    path('add-expense', add_expense, name='add_expense'),
    path("expense/success/", expense_success, name="expense_success"),


]
