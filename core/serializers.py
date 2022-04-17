from rest_framework import serializers

from core import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name', 'limit']


class CostListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category_id.name')

    class Meta:
        model = models.Cost
        fields = ['id', 'name', 'amount', 'category_name']


class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cost
        fields = ['id', 'name', 'amount', 'category_id']


class TelegramCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cost
        fields = ['id', 'name', 'amount', 'telegram_user_id']
