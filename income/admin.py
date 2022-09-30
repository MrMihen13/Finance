from django.contrib import admin

from income import models


admin.site.register(models.MandatoryExpenses)
admin.site.register(models.FinancialIncomeCategory)
admin.site.register(models.FinancialIncome)
admin.site.register(models.DeductionsFunds)
