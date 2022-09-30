import datetime


def get_next_month_url(request, month_end: datetime):
    url = _remove_empty_items(request.build_absolute_uri().split('/'))
    next_month = month_end + datetime.timedelta(days=1)

    url_next_month = url.pop(0) + '//'

    for item in url:
        if item.isdigit():
            break
        url_next_month += item + '/'

    if (next_month.month - datetime.datetime.now().month) > 1 and next_month.year == datetime.datetime.now().year:
        return None

    return url_next_month + f'{next_month.month}/{next_month.year}/'


def get_prev_month_url(request, month_start: datetime):
    url = _remove_empty_items(request.build_absolute_uri().split('/'))
    prev_month = month_start - datetime.timedelta(days=1)

    url_prev_month = url.pop(0) + '//'

    for item in url:
        if item.isdigit():
            break
        url_prev_month += item + '/'

    return url_prev_month + f'{prev_month.month}/{prev_month.year}/'


def _remove_empty_items(array: list):
    for item in array:
        array.remove(item) if item == '' else None
    return array
