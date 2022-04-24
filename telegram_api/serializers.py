from rest_framework import serializers

from core import models


class TelegramCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cost
        fields = ['id', 'name', 'amount', 'telegram_uid']
