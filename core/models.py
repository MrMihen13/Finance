from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name', blank=False, null=False)
    limit = models.DecimalField(verbose_name='Limit', max_digits=12, decimal_places=2, blank=True, null=True)


