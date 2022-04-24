import logging

from rest_framework import generics, response, status, permissions

from core import models
from core.permissions import IsOwner
from telegram_api import serializers
from telegram_api.permissions import HasTelegramToken


logger = logging.getLogger(__name__)


class CostListTelegramAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.TelegramCostSerializer
    queryset = models.Cost.objects.all()

    def get(self, request, *args, **kwargs):
        if request.data.get('uid') is None:
            return response.Response(data={'error': 'user_id is None'}, status=status.HTTP_400_BAD_REQUEST)
        data = self.queryset.filter(telegram_user_id=request.data.get('uid'))
        serializer = self.serializer_class(data=data, many=True)
        serializer.is_valid()
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)


class CostCreateTelegramAPI(generics.CreateAPIView):  # TODO Изменить сохранение данных
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.TelegramCostSerializer
    queryset = models.Cost.objects.all()

    def post(self, request, *args, **kwargs):
        if request.data.get('telegram_uid') is None:
            return response.Response(data={'error': 'user_id is None'}, status=status.HTTP_400_BAD_REQUEST)
        data = self.queryset.create(
            telegram_uid=request.data.get('telegram_uid'),
            name=request.data.get('name'),
            amount=request.data.get('amount')
        )
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
        return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CostRetrieveUpdateDestroyTelegramAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, IsOwner)
    serializer_class = serializers.TelegramCostSerializer
    queryset = models.Cost.objects.all()

    def put(self, request, *args, **kwargs):
        ...

    def patch(self, request, *args, **kwargs):
        ...

    def destroy(self, request, *args, **kwargs):
        ...


class CategoryListTelegramAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.TelegramCostSerializer
    queryset = models.Category.objects.all()

    def get(self, request, *args, **kwargs):
        if request.data.get('telegram_uid') is None:
            return response.Response(data={'error': 'user_id is None'}, status=status.HTTP_400_BAD_REQUEST)
        data = self.queryset.filter(telegram_user_id=request.data.get('uid'))
        serializer = self.serializer_class(data=data, many=True)
        serializer.is_valid()
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)


class CategoryCreateTelegramAPI(generics.CreateAPIView):
    permission_classes = ()
    serializer_class = serializers.TelegramCostSerializer
    queryset = models.Category.objects.all()

    def post(self, request, *args, **kwargs):
        if request.data.get('telegram_uid') is None:
            return response.Response(data={'error': 'user_id is None'}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            'telegram_uid': request.data.get('telegram_uid'),
            'name': request.data.get('name'),
            'amount': request.data.get('amount'),
        }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
        return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CategoryRetrieveUpdateDestroyTelegramAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner, )
    serializer_class = serializers.TelegramCostSerializer
    queryset = models.Category.objects.all()

    def put(self, request, *args, **kwargs):
        ...

    def patch(self, request, *args, **kwargs):
        ...

    def destroy(self, request, *args, **kwargs):
        ...
