import datetime

from django.utils import timezone


def get_month_end(date: datetime):
    """Getting last date of month"""
    next_month = date.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)


def get_month_start(month: int = None, year: int = None):
    """Getting month start"""
    if month is None and year is None:
        month_start = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    else:
        month_start = timezone.datetime(day=1, month=month, year=year)
    return month_start
