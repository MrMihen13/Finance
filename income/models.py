from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class FinancialIncomeCategory(models.Model):
    name = models.CharField(max_length=128)


class FinancialIncome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(FinancialIncomeCategory, on_delete=models.DO_NOTHING, null=True, blank=True)
    income = models.PositiveIntegerField()
    net_income = models.PositiveIntegerField()

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        mandatory_expenses = MandatoryExpenses.objects.filter(user=self.user).all()
        mandatory_expenses = mandatory_expenses.aggregate(models.Sum('amount'))
        mandatory_expenses = mandatory_expenses['amount__sum']
        if self.income:
            self.net_income = self.income


class MandatoryExpenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()


class DeductionsFunds(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = ...
    percent = ...

