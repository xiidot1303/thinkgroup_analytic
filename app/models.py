from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Expense(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    staff = models.ForeignKey('bot.Staff', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.branch.name} - {self.category.name} - {self.amount}"