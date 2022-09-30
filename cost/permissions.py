from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.pk == request.user


class OnlyProfessionalRatePlan(permissions.BasePermission):
    message = {
        'errors': 'Rate plan error',
        'message': 'Ваш тарифный план не включает в себя данную функцию. '
    }

    def has_permission(self, request, view):
        return request.user.rate_plan == 'professional'


class BaseOrProfessionalRatePlan(permissions.BasePermission):
    message = {
        'errors': 'Rate plan error',
        'message': 'Ваш тарифный план не включает в себя данную функцию.'
    }

    def has_permission(self, request, view):
        return request.user.rate_plan != 'free'
