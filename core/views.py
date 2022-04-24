import logging

from django.utils import timezone
from django.db.models import Sum

from rest_framework import generics, permissions, response, status

from core import models, serializers
from core import permissions as custom_permissions

logger = logging.getLogger(__name__)


class CostListApiView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.CostListSerializer
    queryset = models.Cost.objects.all()

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user_id=user.id)

    def list(self, request, *args, **kwargs):  # TODO Добавить пагинацию
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return response.Response(status=status.HTTP_200_OK, data=serializer.data)


class CostRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, custom_permissions.IsOwner)
    serializer_class = serializers.CostSerializer

    def get_queryset(self):
        return models.Cost.objects.all()


class CategoryRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, custom_permissions.IsOwner)
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return models.Category.objects.all()


class CostCreateApiView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.CostSerializer
    queryset = models.Cost.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
        return response.Response(status=status.HTTP_201_CREATED, data=serializer.data)


class CategoryListApiView(generics.ListAPIView):  # TODO Добавить пагинацию
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return response.Response(status=status.HTTP_200_OK, data=serializer.data)


class CategoryCreateApiView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
        return response.Response(status=status.HTTP_201_CREATED, data=serializer.data)


class GetAnalyticsApiView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.CostSerializer

    def get_queryset(self):
        return models.Cost.objects.filter(user_id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        month_start = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        current_date = timezone.now()

        costs = self.get_queryset().filter(created_at__gte=month_start, created_at__lte=current_date)
        categories = models.Category.objects.filter(user_id=self.request.user.id)

        total = costs.aggregate(Sum('amount'))

        data = {'sum': total['amount__sum']}

        for obj in categories:
            amount = costs.filter(category_id=obj.id).aggregate(Sum('amount'))
            percent = round((amount['amount__sum'] * 100) / total['amount__sum'])
            data[obj.name] = {'total': amount['amount__sum'], 'percent': percent}

        return response.Response(data=data, status=status.HTTP_200_OK)
