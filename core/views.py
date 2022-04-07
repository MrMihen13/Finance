import logging

from rest_framework import generics, permissions, response, status, decorators, renderers

from core import models, serializers
from core import custom_permissions

logger = logging.getLogger(__name__)


class CostListApiView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.CostListSerializer
    queryset = models.Cost.objects.all()

    def list(self, request, *args, **kwargs):
        costs = self.queryset.filter(user_id=request.user.id)
        serializer = self.serializer_class(costs, many=True)
        return response.Response(status=status.HTTP_200_OK, data=serializer.data)


class CreateCostApiView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, custom_permissions.IsOwner)
    serializer_class = serializers.CostSerializer
    queryset = models.Cost.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
        return response.Response(status=status.HTTP_200_OK, data=serializer.data)


class RetrieveCostApiView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, custom_permissions.IsOwner)
    serializer_class = serializers.CostSerializer
    queryset = models.Cost.objects.all()


class CategoryListApiView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

    def list(self, request, *args, **kwargs):
        categories = self.queryset.filter(user_id=request.user.id)
        serializer = self.serializer_class(categories, many=True)
        return response.Response(status=status.HTTP_200_OK, data=serializer.data)


class CreateCategoryApiView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
        return response.Response(status=status.HTTP_200_OK, data=serializer.data)


class RetrieveCategoryApiView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, custom_permissions.IsOwner)
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
