from django.contrib import admin

from cauth import models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_active', 'telegram_uid')
    list_filter = ('is_active', 'is_superuser')
