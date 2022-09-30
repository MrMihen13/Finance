from rest_framework import serializers

from cost import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name']


class CostListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category_id.name')
    date = serializers.DateTimeField(source='created_at', format="%Y-%m-%d %H:%M")

    class Meta:
        model = models.Cost
        fields = ['id', 'date', 'name', 'amount', 'category_name']


class CostSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category_id.name', read_only=True)
    date = serializers.DateTimeField(source='created_at', format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = models.Cost
        fields = ['id', 'date', 'name', 'amount', 'category_id', 'category_name']


class ExcelExportSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category_id.name', read_only=True)
    date = serializers.DateTimeField(source='created_at', format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = models.Cost
        fields = ['date', 'name', 'amount', 'category_name']
