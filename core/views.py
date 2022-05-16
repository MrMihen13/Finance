# TODO Написать краткое описание для каждого класса и функции
import datetime
import logging

from django.utils import timezone
from django.db.models import Sum
from django_filters import rest_framework

from rest_framework import generics, status, response
from rest_framework.permissions import IsAuthenticated

from core import models, serializers, pagination
from core import permissions as custom_permissions
from core.utils.date_utils import get_month_end, get_month_start
from core.utils.url_utils import get_next_month_url, get_prev_month_url

logger = logging.getLogger(__name__)


class CostListApiView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CostListSerializer
    pagination_class = pagination.PaginationWithMonth
    filter_backends = [rest_framework.DjangoFilterBackend, ]
    filterset_fields = ['category_id']
    view_path = '/costs/'

    def get_queryset(self):
        user = self.request.user
        return models.Cost.objects.filter(user_id=user.id)

    def get(self, request, *args, **kwargs):

        if self.kwargs.get('month') is None and self.kwargs.get('year') is None:
            month_start = get_month_start(timezone.now())
        else:
            month_start = timezone.datetime(day=1, month=self.kwargs.get('month'), year=self.kwargs.get('year'))

        month_end = get_month_end(month_start)

        costs = self.get_queryset().filter(created_at__gte=month_start.date(), created_at__lte=month_end)

        if request.GET.get('category_id'):
            costs = costs.filter(category_id=request.GET.get('category_id'))

        serializer = self.serializer_class(costs, many=True)
        page = self.paginate_queryset(serializer.data)

        data = self.get_paginated_response(page)

        data.data['links']['next_month'] = get_next_month_url(request=request, month_end=month_end)
        data.data['links']['prev_month'] = get_prev_month_url(request=request, month_start=month_start)

        return data


class CostRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, custom_permissions.IsOwner)
    serializer_class = serializers.CostSerializer

    def get_queryset(self):
        return models.Cost.objects.all()


class CategoryRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, custom_permissions.IsOwner)
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return models.Category.objects.all()


class CostCreateApiView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CostSerializer
    queryset = models.Cost.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
        return response.Response(status=status.HTTP_201_CREATED, data=serializer.data)


class CategoryListApiView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return models.Category.objects.filter(user_id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)


class CategoryCreateApiView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
        return response.Response(status=status.HTTP_201_CREATED, data=serializer.data)


class GetAnalyticsApiView(generics.GenericAPIView):  # TODO Добавить тесты
    """Getting cost`s analytics for month"""
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CostSerializer
    view_path = '/analytics/'

    def get_queryset(self):
        return models.Cost.objects.filter(user_id=self.request.user.id)

    def get(self, request, month=None, year=None, *args, **kwargs):
        if month is None and year is None:
            month_start = get_month_start(timezone.now())
        else:
            month_start = timezone.datetime(day=1, month=month, year=year)

        month_end = get_month_end(month_start)

        costs = self.get_queryset().filter(created_at__gte=month_start.date(), created_at__lte=month_end)
        categories = models.Category.objects.filter(user_id=self.request.user.id)
        full_amount = costs.aggregate(Sum('amount'))
        print(categories)

        data = {
            'links': dict(
                next_month=get_next_month_url(request=request,month_end=month_end),
                prev_month=get_prev_month_url(request=request, month_start=month_start)
            ),
            'results': dict(
                full_amount=full_amount['amount__sum'], month_name=month_start.strftime('%B'), categories=[]
            ),
        }

        if full_amount['amount__sum']:

            for obj in categories:
                category_amount = costs.filter(category_id=obj.id).aggregate(Sum('amount'))

                if category_amount['amount__sum']:
                    percent = round((category_amount['amount__sum'] * 100) / full_amount['amount__sum'])

                    data['results']['categories'].append({
                        'id': obj.id, 'name': obj.name, 'total': category_amount['amount__sum'], 'percent': percent
                    })

        return response.Response(data=data, status=status.HTTP_200_OK)


# TODO Апгрейд тарифного плана
# TODO Добавить тесты для обновления тарифного плана

# TODO Добавить экспорт данных в Excel
