from datetime import datetime

from django.db.models import Sum, QuerySet

from cauth.models import CustomUser
from cost.models import Cost, Category

from cost.utils.date_utils import get_month_start, get_month_end
from cost.utils.url_utils import add_months_navigation_links


class AnalyticsServices:
    month_start: datetime
    month_end: datetime
    costs: QuerySet(Cost)
    categories: QuerySet(Category)

    request = None

    def __init__(self, user: CustomUser, queryset: QuerySet(Cost), request,  month: int = None, year: int = None):
        self.month_start = get_month_start(month=month, year=year)
        self.month_end = get_month_end(self.month_start)

        self.costs = queryset.filter(created_at__gte=self.month_start.date(), created_at__lte=self.month_end, user=user)
        self.categories = Category.objects.filter(user=user)
        self.request = request

    @property
    def all_cost_analytics_data(self) -> dict:
        full_amount = self.costs.aggregate(Sum('amount'))

        data: dict = dict()
        
        data = add_months_navigation_links(
            data=data, request=self.request, month_start=self.month_start, month_end=self.month_end)

        data['results'] = dict(
                full_amount=full_amount['amount__sum'], month_name=self.month_start.strftime('%B'), categories=[])

        if full_amount['amount__sum']:
            data = self._generate_analytics(data, full_amount['amount__sum'])

        return data

    def _generate_analytics(self, data: dict, full_amount: int) -> dict:
        for obj in self.categories:
            category_amount = self.costs.filter(category_id=obj.id).aggregate(Sum('amount'))

            if category_amount['amount__sum']:
                percent = round((category_amount['amount__sum'] * 100) / full_amount)

                data['results']['categories'].append({
                    'id': obj.id, 'name': obj.name, 'total': category_amount['amount__sum'], 'percent': percent})

        return data
