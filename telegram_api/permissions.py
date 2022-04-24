from rest_framework import permissions

from django.conf import settings


class HasTelegramToken(permissions.BasePermission):
    def has_permission(self, request, view):
        return settings.TELEGRAM['TOKEN'] == request.headers.get('Telegram-token')