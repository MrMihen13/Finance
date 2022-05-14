import datetime


def get_month_end(date: datetime):
    """Getting last date of month"""
    next_month = date.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)


def get_month_start(date: datetime):
    """Getting month start"""
    return date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
