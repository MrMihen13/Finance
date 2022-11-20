from django.db.models import QuerySet
from django.conf import settings

from rest_framework import status
from rest_framework.serializers import ModelSerializer

from cost import models
from cauth.models import CustomUser


class _Response:
    status: status
    data: dict


class CategoryServices:
    @staticmethod
    def save_category(user: CustomUser, request, queryset: QuerySet(models.Cost), serializer_class: ModelSerializer) -> _Response:
        response = _Response

        if settings.USER_CATEGORY_LIMIT >= queryset.filter(user_id=request.user.id).count():
            data = request.data
            serializer = serializer_class(data=data)

            if serializer.is_valid():
                serializer.save(user_id=request.user)

            response.status = status.HTTP_201_CREATED
            response.data = serializer.data

            return response
        
        response.status = status.HTTP_423_LOCKED
        response.data = {'error': 'Category limit exceeded', 'message': 'Вы создали максимальное количество категорий'}
        
        return response