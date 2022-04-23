import logging

from rest_framework import generics, response, status

from core import serializers, custom_permissions, models


logger = logging.getLogger(__name__)


class AddCostTelegramAPI(generics.CreateAPIView):
    serializer_class = serializers.TelegramCostSerializer
    permission_classes = (custom_permissions.HasTelegramToken, )
    queryset = models.Cost.objects.all()

    def post(self, request, *args, **kwargs):
        if request.data.get('telegram_user_id') is None:
            return response.Response(data={'error': 'user_id is None'}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            'telegram_user_id': request.data.get('telegram_user_id'),
            'name': request.data.get('name'),
            'amount': request.data.get('amount'),
        }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
        return response.Response(data={'msg': 'Successful'}, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        if request.data.get('telegram_user_id') is None:
            return response.Response(data={'error': 'user id is not provided'}, status=status.HTTP_400_BAD_REQUEST)
        cost = self.queryset.filter(user_id__telegram_id=request.data.get('telegram_user_id')).first()
        serializer = self.serializer_class(data=cost)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)


class CostListTelegramAPI(generics.ListAPIView):
    permission_classes = (custom_permissions.HasTelegramToken, )
    serializer_class = serializers.TelegramCostSerializer
    queryset = models.Cost.objects.all()

    def get(self, request, *args, **kwargs):
        if request.data.get('telegram_user_id') is None:
            return response.Response(data={'error': 'user_id is None'}, status=status.HTTP_400_BAD_REQUEST)
        data = self.queryset.filter(telegram_user_id=request.data.get('telegram_user_id'))
        serializer = self.serializer_class(data=data, many=True)
        serializer.is_valid()
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

