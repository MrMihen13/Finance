import logging

from django_filters import rest_framework
from django.conf import settings
from django.http import HttpResponse

from rest_framework import generics, status, response
from rest_framework.permissions import IsAuthenticated

from cost import models, serializers
from cost import permissions as custom_permissions
from cost.utils.date_utils import get_month_end, get_month_start
from cost.utils.url_utils import add_months_navigation_links
from cost.services.analytics_services import AnalyticsServices
from cost.services.cost_services import ExcelServices, CostServices
from cost.services.category_services import CategoryServices

logger = logging.getLogger(__name__)


class CostListApiView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CostListSerializer
    filter_backends = [rest_framework.DjangoFilterBackend, ]
    filterset_fields = ['category_id']

    def get_queryset(self):
        user = self.request.user
        return models.Cost.objects.filter(user_id=user.id)

    def get(self, request, month=None, year=None, *args, **kwargs):
        month_start = get_month_start(month=month, year=year)
        month_end = get_month_end(month_start)

        costs = CostServices.get_costs(
            queryset=self.get_queryset(), serializer_class=self.serializer_class, 
            category_id=self.request.GET.get('category_id'), month=month, year=year)

        page = self.paginate_queryset(costs)
        data = self.get_paginated_response(page)

        data = add_months_navigation_links(data=data.data, request=self.request, month_start=month_start, month_end=month_end)

        return response.Response(data=data, status=status.HTTP_200_OK)


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


class CategoryCreateApiView(generics.CreateAPIView):  # TODO Тесты
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

    def post(self, request, *args, **kwargs):
        _response = CategoryServices.save_category(
            user=self.request.user, request=self.request, queryset=self.queryset, 
            serializer_class=self.serializer_class)

        return response.Response(status=_response.status, data=_response.data)


class GetAnalyticsApiView(generics.GenericAPIView):
    """Getting cost`s analytics for month"""
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CostSerializer

    def get_queryset(self):
        return models.Cost.objects.filter(user_id=self.request.user.id)

    def get(self, request, month=None, year=None, *args, **kwargs):
        analytics = AnalyticsServices(
            user=self.request.user, queryset=self.get_queryset(), request=self.request, month=month, year=year)

        data = analytics.all_cost_analytics_data

        return response.Response(data=data, status=status.HTTP_200_OK)


class UpgradeRatePlanApiView(generics.GenericAPIView):  # TODO Тесты
    ...  # TODO Апгрейд тарифного плана


class ExelExportApiView(generics.GenericAPIView):  # TODO Тесты
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ExcelExportSerializer

    def get_queryset(self):
        return models.Cost.objects.filter(user_id=self.request.user.id)

    def get(self, request, month=None, year=None, *args, **kwargs):

        excel_services = ExcelServices(
            queryset=self.get_queryset(), serializer_class=self.serializer_class, month=month, year=year)

        workbook = excel_services.workbook

        _response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        _response['Content-Disposition'] = f'attachment; filename="costs-{excel_services.month_start.strftime("%B-%Y").lower()}.xlsx"'

        workbook.save(_response)

        return _response
