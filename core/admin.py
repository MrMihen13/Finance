from django.contrib import admin

from core import models


@admin.register(models.Cost)
class CostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_id', 'user_id')
    list_filter = ('category_id', 'user_id')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'limit', 'user_id')


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_active', 'telegram_id', 'discord_id')
    list_filter = ('is_active', 'is_superuser')
