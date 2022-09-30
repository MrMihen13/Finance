from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name', blank=False, null=False)
    limit = models.DecimalField(verbose_name='Limit', max_digits=12, decimal_places=2, blank=True, null=True)
    user_id = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Cost(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name', blank=False, null=False)
    amount = models.DecimalField(verbose_name='Amount', max_digits=12, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Date', default=timezone.now, editable=False)
    category_id = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE, blank=True, null=True)
    user_id = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, blank=True, null=True)
    telegram_uid = models.CharField(max_length=10, verbose_name='Telegram User Id', blank=True, null=True)

    def __str__(self):
        return self.name
