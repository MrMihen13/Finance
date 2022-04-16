from rest_framework import generics, permissions

from core import serializers, custom_permissions, models


class AddCostTelegramAPI(generics.CreateAPIView):
    serializer_class = serializers.CostSerializer
    permission_classes = (custom_permissions.HasTelegramToken, )
    queryset = models.Cost.objects.all()


class CostListTelegramAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.CostListSerializer

    def queryset(self, request, *args, **kwargs):
        return models.Cost.objects.filter(user_id__telegram_id=request.data['user_id']).all()
