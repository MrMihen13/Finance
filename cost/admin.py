from django.contrib import admin

from cost import models


@admin.register(models.Cost)
class CostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_id', 'user_id', 'amount')
    list_filter = ('category_id', 'user_id')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'limit', 'user_id')

    def get_queryset(self, request):
        queryset = super(CategoryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(user_id=request.user.id)
