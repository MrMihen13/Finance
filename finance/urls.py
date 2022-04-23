"""
finance URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from docs_api import routers_v1 as docs_v1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('core.urls')),
    path('telegram/api/v1/', include('telegram_api.urls')),
    path('docs/', include(docs_v1)),
]
