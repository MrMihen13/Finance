"""
finance URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Finance view')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('core.urls')),
    path('telegram/api/v1/', include('telegram_api.urls')),
    path('swagger', schema_view),
]
