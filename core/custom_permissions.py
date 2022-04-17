from rest_framework import permissions

from django.conf import settings


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.pk == request.user


class HasTelegramToken(permissions.BasePermission):
    def has_permission(self, request, view):
        return settings.TELEGRAM['TOKEN'] == request.headers.get('Telegram-token')

